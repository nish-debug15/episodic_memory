
from memory.episodic.models import EpisodicSummary, EmotionalSignature


def build_episode_summary(
    primary_emotion: str,
    intensity: float,
    trend: str,
    themes: list,
    inferred_needs: list,
    intervention: str,
    outcome: str,
    confidence: float,
) -> EpisodicSummary:

    signature = EmotionalSignature(
        primary=primary_emotion,
        intensity=intensity,
        trend=trend,
    )

    summary = EpisodicSummary(
        emotional_signature=signature,
        themes=themes[:5],
        inferred_needs=inferred_needs[:5],
        intervention=intervention,
        outcome=outcome,
        confidence=confidence,
    )

    if not summary.is_valid():
        raise ValueError("Invalid episodic summary generated")

    return summary
