from pydantic import BaseModel, Field, ValidationError, model_validator
from datetime import datetime
from typing_extensions import Self
from enum import Enum


class Rank(Enum):
    cadet = 1
    officer = 2
    lieutenant = 3
    captain = 4
    commander = 5


class CrewMember(BaseModel):
    member_id: str = Field(..., min_length=3, max_length=10)
    name: str = Field(..., min_length=2, max_length=50)
    rank: Rank
    age: int = Field(..., ge=18, le=80)
    specialization: str = Field(..., min_length=3, max_length=30)
    years_experience: int = Field(..., ge=0, le=50)
    is_active: bool = True


class SpaceMission(BaseModel):
    mission_id: str = Field(..., min_length=5, max_length=15)
    mission_name: str = Field(..., min_length=3, max_length=100)
    destination: str = Field(..., min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(..., ge=1, le=3650)
    crew: list[CrewMember] = Field(..., min_length=1, max_length=12)
    mission_status: str = "planned"
    budget_millions: float = Field(..., ge=1.0, le=10000.0)

    @model_validator(mode='after')
    def mission_validation_rules(self) -> Self:
        if not self.mission_id.startswith("M"):
            raise ValueError("Mission ID must start with \"M\"")

        if not any(c.rank in {Rank.commander, Rank.captain} for c in self.crew):
            raise ValueError("Must have at least one Commander or Captain")

        if self.duration_days > 365:
            expe = 0
            for c in self.crew:
                expe += c.years_experience
            if expe < 5:
                raise ValueError("Long missions (> 365 days) need 50% "
                                 "experienced crew (5+ years)")

        for c in self.crew:
            if c.is_active == False:
                raise ValueError("All crew members must be active")

        return self


def print_info(s: SpaceMission) -> None:
    print(f"Mission: {s.mission_name}")
    print(f"ID: {s.mission_id}")
    print(f"Destination: {s.destination}")
    print(f"Duration: {s.duration_days} days")
    print(f"Budget: ${s.budget_millions}M")
    print(f"Crew size: {len(s.crew)}")
    print("Crew members:")
    for i in s.crew:
        print(f"- {i.name} ({i.rank}) - {i.specialization}")


if __name__ == "__main__":
    try:
        print("Space Mission Crew Validation")
        print("=========================================")
        print("Valid mission created:")

        crew_list = [
            CrewMember(member_id="sarah_001",
                        name="Sarah Connor",
                        rank=Rank.commander,
                        age=34,
                        specialization="Mission Command",
                        years_experience=5,
                        is_active=True),

            CrewMember(member_id="john_002",
                        name="John Smith",
                        rank=Rank.lieutenant,
                        age=55,
                        specialization="Navigation",
                        years_experience=5,
                        is_active=True),

            CrewMember(member_id="alice_001",
                        name="Alice Johnson",
                        rank=Rank.officer,
                        age=43,
                        specialization="Engineering",
                        years_experience=5,
                        is_active=True)
        ]

        mission = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date=datetime.now(),
            duration_days=900,
            crew=crew_list,
            mission_status="Active",
            budget_millions=2500.0
        )
        print_info(mission)
    except ValidationError as e:
        print("Expected validation error:")
        print(e.errors()[0]['msg'])

    print("\n=========================================")

    try:
        SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date=datetime.now(),
            duration_days=900,
            crew=[CrewMember(member_id="alice_001",
                    name="Alice Johnson",
                    rank=Rank.cadet,
                    age=43,
                    specialization="Engineering",
                    years_experience=5,
                    is_active=True)],
            mission_status="Active",
            budget_millions=2500.0
        )
    except ValidationError as e:
        print("Expected validation error:")
        print(e.errors()[0]['msg'])


"""
Space Mission Crew Validation
=========================================
Valid mission created:
Mission: Mars Colony Establishment
ID: M2024_MARS
Destination: Mars
Duration: 900 days
Budget: $2500.0M
Crew size: 3
Crew members:
- Sarah Connor (commander) - Mission Command
- John Smith (lieutenant) - Navigation
- Alice Johnson (officer) - Engineering

=========================================
Expected validation error:
Mission must have at least one Commander or Captain """