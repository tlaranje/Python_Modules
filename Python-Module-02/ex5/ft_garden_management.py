
class GardenManager:
    """Manage plants and water resources in the garden."""
    def __init__(self):
        """Initialize the garden with an empty plant list and water tank."""
        self.plants = []
        self.tank = 2

    def add_plant(self, p):
        """Add a plant to the garden, raising an error if its name is empty."""
        if not p.name:
            raise PlantError("Plant name cannot be empty!")
        print(f"Added {p.name} successfully")
        self.plants.append(p)

    def water_plants(self, water):
        """Water plants, raise an error if tank dont have sufficient water."""
        for p in self.plants:
            if self.tank - water >= 0:
                p.water += water
                self.tank -= water
                print(f"Watering {p.name} - success")
            else:
                raise GardenError("Not enough water in tank")

    def check_plant_health(self):
        """Check plant health and raise errors for water or sunlight issues."""
        for p in self.plants:
            if p.water > 10:
                raise PlantError(
                    f"{p.name} has died, water level {p.water} "
                    "is too high (max 10).")
            elif p.water < 0:
                raise PlantError(
                    f"{p.name} water level {p.water} is too low (min 1), "
                    "increase watering to maintain plant health.")

            if p.sun > 10:
                 raise PlantError(
                    f"{p.name} sunlight days is to high (max 10), "
                    "consider moving the plant to a shaded area.")
            elif p.sun < 1:
                raise PlantError(
                    f"{p.name} sunlight days {p.sun} is too low (min 1), "
                    "move the plant to a brighter location.")
            print(f"{p.name}: healthy (water: {p.water}, sum: {p.sun})")


class Plant:
    """Represent a plant with name, water level, and sunlight value."""
    def __init__(self, name, water, sun):
        """Initialize a plant with name, water level, and sunlight hours."""
        self.name = name
        self.water = water
        self.sun = sun


class GardenError(Exception):
    """Base class for garden-related errors."""
    def __init__(self, msg):
        super().__init__(msg)


class PlantError(GardenError):
    """Error raised for plant-specific problems."""
    def __init__(self, msg):
        super().__init__(msg)


if __name__ == "__main__":
    print("=== Garden Management System ===\n")
    garden = GardenManager()

    print("Adding plants to garden...")
    try:
        garden.add_plant(Plant("Tomato", 5, 8))
        garden.add_plant(Plant("Lettuce", 5, 20))
        garden.add_plant(Plant("", 9, 8))
    except PlantError as e:
        print(f"Error adding plant: {e}")

    print("\nWatering plants...\nOpening watering system")
    try:
        garden.water_plants(1)
    except GardenError as e:
        print(f"Caught GardenError: {e}")
    finally:
        print("Closing watering system (cleanup)")

    print("\nChecking plant health...")
    try:
        garden.check_plant_health()
    except PlantError as e:
        print(f"Error checking: {e}")

    print("\nTesting error recovery...")
    try:
        if garden.tank <= 0:
            raise GardenError("Not enough water in tank")
    except GardenError as e:
        print(f"Caught GardenError: {e}")

    print("System recovered and continuing...")
    print("\nGarden management system test complete!")
