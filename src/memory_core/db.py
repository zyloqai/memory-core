import sqlite3
from pathlib import Path


# Default database used by the real application.
DB_PATH = Path("memory.db")


def get_connection(db_path: Path | str = DB_PATH):
    """
    Open a SQLite connection.

    Why allow db_path?
    - production/demo code can use memory.db
    - tests can use their own temporary database
    """
    return sqlite3.connect(db_path)


def init_db(db_path: Path | str = DB_PATH):
    """
    Create the evidence table if it does not exist.
    """

    conn = get_connection(db_path)

    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS interactions (
            interaction_id TEXT PRIMARY KEY,
            parent_id TEXT NOT NULL,
            student_id TEXT,
            channel TEXT NOT NULL,
            timestamp TEXT NOT NULL,
            messages_json TEXT NOT NULL
        )
        """
    )

    conn.commit()
    conn.close()