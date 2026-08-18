from memory_core.db import init_db
from memory_core.models import Interaction, Message
from memory_core.store import get_interactions, save_interaction


def test_parent_interactions_can_be_retrieved(tmp_path):
    """
    The test creates its own isolated SQLite database.

    tmp_path is provided by pytest and disappears after the test.
    """

    test_db = tmp_path / "test_memory.db"

    init_db(test_db)

    interaction = Interaction(
        interaction_id="INT-TEST-001",
        parent_id="PAR-001",
        student_id="STU-001",
        channel="PHONE",
        timestamp="2026-08-17T10:00:00",
        messages=[
            Message(
                speaker="parent",
                text="Tara is currently in UKG."
            )
        ],
    )

    # Seed the test database ourselves.
    save_interaction(interaction, test_db)

    history = get_interactions("PAR-001", test_db)

    assert len(history) == 1
    assert history[0].interaction_id == "INT-TEST-001"