from pydantic import BaseModel, Field, ValidationError, model_validator
from datetime import datetime
from typing import Optional
from typing_extensions import Self
from enum import Enum


class ContactType(Enum):
    radio = 0
    visual = 1
    physical = 2
    telepathic = 3


class AlienContact(BaseModel):
    contact_id: str = Field(..., min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(..., min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(..., ge=0.0, le=10.0)
    duration_minutes: int = Field(..., ge=1, le=1440)
    witness_count: int = Field(..., ge=1, le=100)
    message_received: Optional[str] = Field(None, max_length=500)
    is_verified: bool = False

    @model_validator(mode='after')
    def check_business_rules(self) -> Self:
        if not self.contact_id.startswith("AC"):
            raise ValueError("Contact ID must start with \"AC\"")

        if self.contact_type == ContactType.physical:
            if self.is_verified is not True:
                raise ValueError("Physical contact reports must be verified")

        if self.contact_type == ContactType.telepathic:
            if self.witness_count is None or self.witness_count < 3:
                raise ValueError(
                    "Telepathic contact requires at least 3 witnesses")

        if self.signal_strength > 7.0:
            if not self.message_received:
                raise ValueError("Strong signals (> 7.0) must include a "
                                    "received message" )
        return self


def print_info(s: AlienContact) -> None:
    print(f"ID: {s.contact_id}")
    print(f"Type: {s.contact_type.name}")
    print(f"Location: {s.location}")
    print(f"Signal: {s.signal_strength}/10")
    print(f"Duration: {s.duration_minutes} minutes")
    print(f"Witnesses: {s.witness_count}")
    print(f"Message: '{s.message_received}'\n")


def main() -> None:
    print("Alien Contact Log Validation")
    print("========================================")

    try:
        station = AlienContact(
            contact_id="AC_2024_001",
            timestamp=datetime.now(),
            location="Area 51, Nevada",
            contact_type=ContactType.radio,
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=5,
            message_received="Greetings from Zeta Reticuli",
            is_verified=True)

        print("Valid contact report:")
        print_info(station)
    except ValidationError as e:
        print("Expected validation error:")
        print(e.errors()[0]['msg'])

    print("========================================")
    try:
        AlienContact(
            contact_id="AC_2024_001",
            timestamp=datetime.now(),
            location="Area 51, Nevada",
            contact_type=ContactType.telepathic,
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=1,
            message_received="Greetings from Zeta Reticuli",
            is_verified=True)
    except ValidationError as e:
        print("Expected validation error:")
        print(e.errors()[0]['msg'])

if __name__ == "__main__":
    main()
