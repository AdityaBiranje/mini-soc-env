from pydantic import BaseModel
from typing import Literal

class Observation(BaseModel):
    log: str
    context: str

class Action(BaseModel):
    decision: Literal["ignore", "flag", "escalate"]
    confidence: float  # NEW

class Reward(BaseModel):
    score: float