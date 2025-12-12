
class GardenManager:
    """Manage plants and water resources in the garden."""
    def __init__(self):
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
                raise GardenError(
                    f"Not enough water in tank to watering {p.name}")

    def check_plant_health(self):
        """Check plant health and raise errors for water or sunlight issues."""
        for p in self.plants:
            if p.water > 10:
                raise PlantError(
                    f"{p.name} has died, water level {p.water} "
                    "is too high (max 10).")
            elif p.water < 1:
                raise PlantError(
                    f"{p.name} water level {p.water} is too low (min 1), "
                    "increase watering to maintain plant health.")

            if p.sun > 13:
                raise PlantError(
                    f"{p.name} sunlight days is to high (max 13), "
                    "consider moving the plant to a shaded area.")
            elif p.sun < 2:
                raise PlantError(
                    f"{p.name} sunlight days {p.sun} is too low (min 2), "
                    "move the plant to a brighter location.")
            print(f"{p.name}: healthy (water: {p.water}, sun: {p.sun})")


class Plant:
    """Represent a plant with name, water level, and sunlight value."""
    def __init__(self, name, water, sun):
        self.name = name
        self.water = water
        self.sun = sun


class GardenError(Exception):
    """Base class for garden-related errors."""
    pass


class PlantError(GardenError):
    """Error raised for plant-specific problems."""
    pass


if __name__ == "__main__":
    print("=== Garden Management System ===\n")
    garden = GardenManager()

    print("Adding plants to garden...")
    try:
        garden.add_plant(Plant("Tomato", 4, 8))
        garden.add_plant(Plant("Lettuce", 10, 13))
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
        print(f"Tank have {garden.tank} liters left!")
    except GardenError as e:
        print(f"Caught GardenError: {e}")

    print("System recovered and continuing...")
    print("\nGarden management system test complete!")
