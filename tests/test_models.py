def test_emotional_signature_valid():
    from memory.episodic.models import EmotionalSignature

    sig = EmotionalSignature("anxiety", 0.5, "stable")
    assert sig.intensity == 0.5
