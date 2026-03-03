import asyncio
from groq import AsyncGroq
from typing import List, Dict
from asyncio_throttle import Throttler
import config

class TargetModel:
    def __init__(self, model_name: str = config.TARGET_MODEL):
        self.model_name = model_name
        self.client = AsyncGroq(api_key=config.GROQ_API_KEY)
        self.throttler = Throttler(rate_limit=config.MAX_CONCURRENT_REQUESTS)
    
    async def single_turn_query(self, prompt: str) -> str:
        async with self.throttler:
            try:
                response = await self.client.chat.completions.create(
                    model=self.model_name,
                    messages=[{"role": "user", "content": prompt}],
                    max_tokens=500,
                    temperature=0.7
                )
                return response.choices[0].message.content
            except Exception as e:
                return f"Error: {str(e)}"
    
    async def multi_turn_query(self, conversation: List[Dict[str, str]]) -> str:
        async with self.throttler:
            try:
                messages = []
                for turn in conversation:
                    messages.append({"role": "user", "content": turn["prompt"]})
                    if "response" in turn:
                        messages.append({"role": "assistant", "content": turn["response"]})
                
                response = await self.client.chat.completions.create(
                    model=self.model_name,
                    messages=messages,
                    max_tokens=500,
                    temperature=0.7
                )
                return response.choices[0].message.content
            except Exception as e:
                return f"Error: {str(e)}"
    
    async def batch_query(self, prompts: List[str]) -> List[str]:
        tasks = [self.single_turn_query(prompt) for prompt in prompts]
        return await asyncio.gather(*tasks)