from datetime import datetime
from typing import Literal

from pydantic import BaseModel


# One useful fact derived from interaction evidence.
class MemoryFact(BaseModel):

    # Unique ID for this memory record.
    memory_id: str

    # The person/entity this fact belongs to.
    # Example: STU-001 or PAR-001.
    subject_id: str

    # Machine-readable fact name.
    # Example: current_grade, preferred_visit_day.
    key: str

    # The actual remembered value.
    value: str

    # Critical for provenance:
    # tells us which interaction produced this memory.
    source_interaction_id: str

    # When this memory was created.
    created_at: datetime

    # Later we will mark old facts as SUPERSEDED
    # when newer information replaces them.
    status: Literal["ACTIVE", "SUPERSEDED"] = "ACTIVE"