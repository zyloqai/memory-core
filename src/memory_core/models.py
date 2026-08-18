from datetime import datetime
from typing import Literal

from pydantic import BaseModel


# One individual utterance inside an interaction.
# Example: Parent says "Tara is currently in UKG."
class Message(BaseModel):
    speaker: Literal["parent", "counsellor"]
    text: str


# One complete interaction with a customer.
# This could eventually come from a phone call, WhatsApp, visit, or email.
class Interaction(BaseModel):

    # Unique ID lets us trace future memories back to this evidence.
    interaction_id: str

    # Connects multiple interactions belonging to the same parent.
    parent_id: str

    # Optional because some conversations may not yet identify the child.
    student_id: str | None = None

    # Knowing the source helps with provenance and auditing later.
    channel: Literal["PHONE", "WHATSAPP", "VISIT", "EMAIL"]

    # Time matters because customer information and preferences can change.
    timestamp: datetime

    # Preserve the original conversation as evidence.
    messages: list[Message]