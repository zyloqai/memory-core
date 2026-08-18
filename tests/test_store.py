from memory_core.db import init_db
from memory_core.store import get_interactions


def test_parent_interactions_can_be_retrieved():
    """
    Milestone 1 test:

    Proves that our evidence store can retrieve the interactions
    previously persisted for a parent.
    """

    init_db()

    history = get_interactions("PAR-001")

    # Our sample parent currently has three stored interactions.
    assert len(history) == 3

    # Evidence should be returned chronologically.
    assert history[0].interaction_id == "INT-001"
    assert history[1].interaction_id == "INT-002"
    assert history[2].interaction_id == "INT-003"