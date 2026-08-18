from memory_core.memory_models import MemoryFact


# We create these manually first.
# Later an LLM will perform this extraction automatically.
sample_memories = [
    MemoryFact(
        memory_id="MEM-001",
        subject_id="STU-001",
        key="current_grade",
        value="UKG",
        source_interaction_id="INT-001",
        created_at="2026-08-17T10:05:00",
    ),

    MemoryFact(
        memory_id="MEM-002",
        subject_id="STU-001",
        key="applying_grade",
        value="Grade 1",
        source_interaction_id="INT-001",
        created_at="2026-08-17T10:05:00",
    ),

    MemoryFact(
        memory_id="MEM-003",
        subject_id="PAR-001",
        key="preferred_visit_day",
        value="Saturday",
        source_interaction_id="INT-002",
        created_at="2026-08-18T14:35:00",
    ),

    MemoryFact(
        memory_id="MEM-004",
        subject_id="PAR-001",
        key="preferred_visit_day",
        value="Sunday",
        source_interaction_id="INT-003",
        created_at="2026-08-20T11:20:00",
    ),
]