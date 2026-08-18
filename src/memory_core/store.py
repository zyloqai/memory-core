import json
from pathlib import Path
from memory_core.memory_models import MemoryFact

from memory_core.db import DB_PATH, get_connection
from memory_core.models import Interaction

def save_memory(
    memory: MemoryFact,
    db_path: Path | str = DB_PATH,
):
    """
    Persist one derived memory fact.

    Important:
    memories are stored separately from raw interaction evidence.
    """

    conn = get_connection(db_path)

    # Duplicate memory IDs should not create duplicate records.
    cursor = conn.execute(
        """
        INSERT OR IGNORE INTO memories (
            memory_id,
            subject_id,
            key,
            value,
            source_interaction_id,
            created_at,
            status
        )
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """,
        (
            memory.memory_id,
            memory.subject_id,
            memory.key,
            memory.value,
            memory.source_interaction_id,
            memory.created_at.isoformat(),
            memory.status,
        ),
    )

    conn.commit()
    created = cursor.rowcount == 1
    conn.close()

    return created


def save_interaction(
    interaction: Interaction,
    db_path: Path | str = DB_PATH,
):
    """
    Save one interaction.

    db_path lets tests use their own database instead of memory.db.
    """

    # IMPORTANT:
    # use the database path passed into this function.
    conn = get_connection(db_path)

    messages_json = json.dumps(
        [message.model_dump() for message in interaction.messages]
    )

    cursor = conn.execute(
        """
        INSERT OR IGNORE INTO interactions (
            interaction_id,
            parent_id,
            student_id,
            channel,
            timestamp,
            messages_json
        )
        VALUES (?, ?, ?, ?, ?, ?)
        """,
        (
            interaction.interaction_id,
            interaction.parent_id,
            interaction.student_id,
            interaction.channel,
            interaction.timestamp.isoformat(),
            messages_json,
        ),
    )

    conn.commit()
    created = cursor.rowcount == 1
    conn.close()

    return created


def get_interactions(
    parent_id: str,
    db_path: Path | str = DB_PATH,
) -> list[Interaction]:
    """
    Retrieve interactions for one parent.

    Using db_path keeps tests isolated from the real application database.
    """

    # Same important rule here:
    # read from the database that was passed in.
    conn = get_connection(db_path)

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
        messages = json.loads(row[5])

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