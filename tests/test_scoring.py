import pytest
import asyncio
from unittest.mock import Mock, patch
from schemas.judge_schema import JudgeScore, AttackResult
from models.judge_model import JudgeModel
from embeddings.embedder import EmbeddingEngine
from attacks.jailbreak_generator import JailbreakGenerator

class TestJudgeModel:
    @pytest.fixture
    def judge_model(self):
        return JudgeModel()
    
    @pytest.mark.asyncio
    async def test_score_interaction_format(self, judge_model):
        # Mock the OpenAI response
        mock_response = Mock()
        mock_response.choices = [Mock()]
        mock_response.choices[0].message.content = '''
        {
            "jailbreak_success": true,
            "violation_score": 4,
            "harmfulness_score": 3,
            "reasoning": "Model provided harmful instructions",
            "confidence": 0.9
        }
        '''
        
        with patch.object(judge_model.client.chat.completions, 'create', return_value=mock_response):
            result = await judge_model.score_interaction("test prompt", "test response")
            
            assert isinstance(result, JudgeScore)
            assert result.jailbreak_success == True
            assert result.violation_score == 4
            assert result.confidence == 0.9

class TestEmbeddingEngine:
    @pytest.fixture
    def embedding_engine(self):
        return EmbeddingEngine()
    
    def test_novelty_detection(self, embedding_engine):
        # Add a text to the store
        test_text = "This is a test attack prompt"
        embedding_engine.add_to_store(test_text)
        
        # Test similar text (should not be novel)
        similar_text = "This is a test attack prompt with minor changes"
        is_novel, similarity = embedding_engine.is_novel(similar_text, threshold=0.7)
        
        # Test very different text (should be novel)
        different_text = "Completely different content about weather"
        is_novel_diff, similarity_diff = embedding_engine.is_novel(different_text, threshold=0.7)
        
        assert similarity > similarity_diff
        assert is_novel_diff == True

class TestJailbreakGenerator:
    @pytest.fixture
    def generator(self):
        return JailbreakGenerator()
    
    def test_generate_attack(self, generator):
        attack = generator.generate_attack()
        
        assert "attack_type" in attack
        assert "prompt" in attack
        assert "harmful_request" in attack
        assert attack["attack_type"] in generator.attack_templates.keys()
    
    def test_generate_multi_turn(self, generator):
        conversation = generator.generate_multi_turn_attack()
        
        assert len(conversation) == 2
        assert conversation[0]["turn"] == 1
        assert conversation[1]["turn"] == 2
        assert "prompt" in conversation[0]
        assert "prompt" in conversation[1]
    
    def test_generate_batch(self, generator):
        batch = generator.generate_batch(5)
        
        assert len(batch) == 5
        for attack in batch:
            assert "attack_type" in attack
            assert "prompt" in attack

if __name__ == "__main__":
    pytest.main([__file__])