from memory_core.models import Interaction, Message


sample_interactions = [
    Interaction(
        interaction_id="INT-001",
        parent_id="PAR-001",
        student_id="STU-001",
        channel="PHONE",
        timestamp="2026-08-17T10:00:00",
        messages=[
            Message(
                speaker="parent",
                text="Hi, I am looking for admission for my daughter Tara."
            ),
            Message(
                speaker="counsellor",
                text="Which grade is she currently studying in?"
            ),
            Message(
                speaker="parent",
                text="She is in UKG and we need Grade 1 admission next year."
            ),
        ],
    ),

    Interaction(
        interaction_id="INT-002",
        parent_id="PAR-001",
        student_id="STU-001",
        channel="WHATSAPP",
        timestamp="2026-08-18T14:30:00",
        messages=[
            Message(
                speaker="parent",
                text="Saturday morning would be best for a campus visit."
            ),
        ],
    ),

    Interaction(
        interaction_id="INT-003",
        parent_id="PAR-001",
        student_id="STU-001",
        channel="PHONE",
        timestamp="2026-08-20T11:15:00",
        messages=[
            Message(
                speaker="parent",
                text="Actually Sunday morning would be easier for us."
            ),
            Message(
                speaker="parent",
                text="Also, do you provide transport near Whitefield?"
            ),
        ],
    ),
]