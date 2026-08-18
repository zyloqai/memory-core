import sqlite3
from pathlib import Path


# Keep the database in the project root.
# SQLite stores everything inside this single file.
DB_PATH = Path("memory.db")


def get_connection():
    """
    Open a connection to SQLite.

    Why this function exists:
    - keeps database connection logic in one place
    - later we can replace SQLite with PostgreSQL more easily
    """
    return sqlite3.connect(DB_PATH)


def init_db():
    """
    Create the interactions table if it does not already exist.

    This is our first persistent evidence store.
    """
    conn = get_connection()

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