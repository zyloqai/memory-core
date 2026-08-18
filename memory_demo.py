from data.sample_memories import sample_memories
from memory_core.db import init_db
from memory_core.store import save_memory


init_db()

for memory in sample_memories:
    created = save_memory(memory)

    if created:
        print(f"Saved {memory.memory_id}")
    else:
        print(f"Skipped duplicate {memory.memory_id}")