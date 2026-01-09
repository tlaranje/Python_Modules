from pydantic import BaseModel, Field, ValidationError
from datetime import datetime
from typing import Optional


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = True
    notes: Optional[str] = Field(default=None, max_length=200)


def info(s: SpaceStation) -> str:
    return (
        f"ID: {s.station_id}\n"
        f"Name: {s.name}\n"
        f"Crew: {s.crew_size}\n"
        f"Power: {s.power_level}%\n"
        f"Oxygen: {s.oxygen_level}%\n"
        "Status: "
        f"{'Operational' if s.is_operational else 'Not Operational'}\n")


def main() -> None:
    print("Space Station Data Validation")
    print("========================================")

    try:
        station = SpaceStation(
            station_id="ISS001",
            name="International Space Station",
            crew_size=6,
            power_level=85.5,
            oxygen_level=92.3,
            last_maintenance=datetime.now(),
            is_operational=True)

        print("Valid Station Created:")
        print(info(station))
    except ValidationError as e:
        print("Expected validation error:")
        for err in e.errors():
            print(f"{err['loc'][0]}: {err['msg']}")

    print("========================================")
    try:
        SpaceStation(
            station_id="BAD01",
            name="Broken Station",
            crew_size=50,
            power_level=50.0,
            oxygen_level=50.0,
            last_maintenance=datetime.now(),
            is_operational=True)

    except ValidationError as e:
        print("Expected validation error:")
        for err in e.errors():
            print(f"{err['loc'][0]}: {err['msg']}")


if __name__ == "__main__":
    main()
