from typing import List
from memory.episodic.models import EpisodicSummary
from memory.episodic.config import RETRIEVAL


def relevance_score(
    episode: EpisodicSummary,
    current_emotion: str,
    current_intensity: float,
) -> float:

    score = 0.0

    if episode.emotional_signature.primary == current_emotion:
        score += 0.4

    intensity_diff = abs(
        episode.emotional_signature.intensity - current_intensity
    )
    score += max(0.0, 0.3 - intensity_diff)

    score += episode.confidence * 0.3

    return min(score, 1.0)


def retrieve_relevant(
    episodes: List[EpisodicSummary],
    current_emotion: str,
    current_intensity: float,
) -> List[EpisodicSummary]:

    scored = [
        (relevance_score(ep, current_emotion, current_intensity), ep)
        for ep in episodes
    ]

    filtered = [
        ep for score, ep in scored if score >= RETRIEVAL["MIN_RELEVANCE"]
    ]

    filtered.sort(
        key=lambda ep: ep.confidence, reverse=True
    )

    return filtered[:RETRIEVAL["TOP_K"]]
