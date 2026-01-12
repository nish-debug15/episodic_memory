def test_retrieval_returns_relevant():
    from memory.episodic.retriever import retrieve_relevant
    from memory.episodic.summarizer import build_episode_summary

    ep = build_episode_summary(
        "anxiety", 0.7, "stable",
        ["meeting"], ["grounding"],
        "pause", "better",
        0.8
    )

    results = retrieve_relevant([ep], "anxiety", 0.65)
    assert len(results) == 1
