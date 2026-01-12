def test_store_add_and_retrieve():
    from memory.episodic.store import EpisodicMemoryStore
    from memory.episodic.summarizer import build_episode_summary

    store = EpisodicMemoryStore()

    ep = build_episode_summary(
        "stress", 0.6, "decreasing",
        ["work"], ["reassurance"],
        "breathing", "calmer",
        0.9
    )

    store.add(ep)
    assert len(store.all()) == 1
