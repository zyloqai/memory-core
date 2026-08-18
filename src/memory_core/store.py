import json

from memory_core.db import get_connection
from memory_core.models import Interaction


def get_interactions(parent_id: str) -> list[Interaction]:
    """
    Load all stored interactions for one parent.

    Why this matters:
    persistence is only useful if we can reconstruct history later.
    """

    conn = get_connection()

    rows = conn.execute(
        """
        SELECT
            interaction_id,
            parent_id,
            student_id,
            channel,
            timestamp,
            messages_json
        FROM interactions
        WHERE parent_id = ?
        ORDER BY timestamp ASC
        """,
        (parent_id,),
    ).fetchall()

    conn.close()

    interactions = []

    for row in rows:
        # Convert stored JSON text back into Python data.
        messages = json.loads(row[5])

        # Rebuild a validated Interaction object.
        interactions.append(
            Interaction(
                interaction_id=row[0],
                parent_id=row[1],
                student_id=row[2],
                channel=row[3],
                timestamp=row[4],
                messages=messages,
            )
        )

    return interactions