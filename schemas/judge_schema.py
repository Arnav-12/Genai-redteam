from pydantic import BaseModel
from typing import List, Optional

class JudgeScore(BaseModel):
    jailbreak_success: bool
    violation_score: int  # 0-5 scale
    harmfulness_score: int  # 0-5 scale
    reasoning: str
    confidence: float  # 0-1 scale

class AttackResult(BaseModel):
    attack_id: str
    attack_type: str
    prompt: str
    response: str
    judge_score: JudgeScore
    embedding: Optional[List[float]] = None
    similarity_score: Optional[float] = None

class ExperimentResult(BaseModel):
    experiment_id: str
    model_name: str
    total_attacks: int
    jailbreak_success_rate: float
    avg_violation_score: float
    avg_harmfulness_score: float
    refusal_rate: float
    results: List[AttackResult]