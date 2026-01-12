from dataclasses import dataclass, field
from typing import List, Dict
from datetime import datetime
import uuid


@dataclass
class EmotionalSignature:
    primary: str
    intensity: float  
    trend: str        


@dataclass
class EpisodicSummary:
    episode_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    timestamp: datetime = field(default_factory=datetime.utcnow)

    emotional_signature: EmotionalSignature = None
    themes: List[str] = field(default_factory=list)
    inferred_needs: List[str] = field(default_factory=list)

    intervention: str = ""
    outcome: str = ""

    confidence: float = 0.0  

    def is_valid(self) -> bool:
        return (
            self.emotional_signature is not None
            and 0.0 <= self.emotional_signature.intensity <= 1.0
            and 0.0 <= self.confidence <= 1.0
        )
