
class GardenError(Exception):
    """Base class for all custom garden-related errors."""
    pass


class PlantError(GardenError):
    """Error raised when a plant-related issue occurs."""
    pass


class WaterError(GardenError):
    """Error raised when a water-related issue occurs."""
    pass


def plant_is_wilting(wilting):
    """Raise a PlantError if the plant is wilting."""
    if wilting is True:
        raise PlantError("The tomato plant is wilting!")
    print("The tomato plant is growing well!")


def check_tank(liters):
    """Raise a WaterError if the water tank has 100 liters or less."""
    if liters <= 100:
        raise WaterError("Not enough water in the tank!")
    print(f"The tank has {liters} liters!")


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===\n")

    try:
        print("Testing PlantError...")
        plant_is_wilting(True)
    except PlantError as e:
        print("PlantError caught:", e)

    print()

    try:
        print("Testing WaterError...")
        check_tank(99)
    except WaterError as e:
        print("WaterError caught:", e)

    print()

    print("Testing catching all garden errors...")
    try:
        plant_is_wilting(True)
    except GardenError as e:
        print("GardenError caught:", e)

    try:
        check_tank(99)
    except GardenError as e:
        print("GardenError caught:", e)

    print("\nAll custom error types work correctly!\n")
