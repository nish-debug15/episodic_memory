from typing import List
from memory.episodic.models import EpisodicSummary
from datetime import datetime, timedelta
from memory.episodic.config import DECAY


class EpisodicMemoryStore:
    def __init__(self):
        self._episodes: List[EpisodicSummary] = []

    def add(self, episode: EpisodicSummary):
        if not episode.is_valid():
            raise ValueError("Attempted to store invalid episode")
        self._episodes.append(episode)

    def all(self) -> List[EpisodicSummary]:
        return list(self._episodes)

    def decay_old_memories(self):
        now = datetime.utcnow()
        for ep in self._episodes:
            age_days = (now - ep.timestamp).days
            if age_days > DECAY["DAYS_UNTIL_DECAY"]:
                ep.confidence *= DECAY["DECAY_FACTOR"]

    def purge_low_confidence(self, threshold: float = 0.2):
        self._episodes = [
            ep for ep in self._episodes if ep.confidence >= threshold
        ]
