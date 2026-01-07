from pydantic import BaseModel, Field, ValidationError, model_validator
from datetime import datetime
from typing import Optional
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

def print_info(s: AlienContact) -> None:
    print(f"ID: {s.station_id}")
    print(f"Name: {s.name}")
    print(f"Crew: {s.crew_size}")
    print(f"Power: {s.power_level}%")
    print(f"Oxygen: {s.oxygen_level}%")
    print("Status: "
          f"{'Operational' if s.is_operational else 'Not Operational'}\n")


def main() -> None:
    print("Space Station Data Validation")
    print("========================================")

    try:
        station = AlienContact(
            station_id="ISS001",
            name="International Space Station",
            crew_size=6,
            power_level=85.5,
            oxygen_level=92.3,
            last_maintenance=datetime.now(),
            is_operational=True)

        print("Valid Station Created:")
        print_info(station)
    except ValidationError as e:
        print("Expected validation error:")
        print(e.errors()[0]['msg'])

    print("========================================")
    try:
        AlienContact(
            station_id="BAD01",
            name="Broken Station",
            crew_size=50,
            power_level=50.0,
            oxygen_level=50.0,
            last_maintenance=datetime.now(),
            is_operational=True)

    except ValidationError as e:
        print("Expected validation error:")
        print(e.errors()[0]['msg'])

if __name__ == "__main__":
    main()
