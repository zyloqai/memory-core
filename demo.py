from memory_core.db import init_db
from memory_core.store import get_interactions


init_db()

# Important: no sample data import here.
# We are proving that previously saved data survives independently.
history = get_interactions("PAR-001")

print(f"Found {len(history)} interactions\n")

for interaction in history:
    print(
        f"{interaction.timestamp} | "
        f"{interaction.channel} | "
        f"{interaction.interaction_id}"
    )

    for message in interaction.messages:
        print(f"  {message.speaker}: {message.text}")

    print()