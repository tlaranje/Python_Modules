
class GardenError(Exception):
    def __init__(self, message="Garden error"):
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message="Plant error"):
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message="Water error"):
        super().__init__(message)


def check_soil(days):
    if days < 30:
        raise GardenError("The soil is not ready for planting, "
                          "the soil needs to rest at last 30 days.")
    print("The soil is ready for planting!")


def check_plant_height(height):
    if height < 0:
        raise PlantError("The height of the plant cannot be negative value.")
    print("The plant has an excellent height!")


def add_water_to_tank(liters):
    max_tank_cap = 1000
    if liters > max_tank_cap:
        raise WaterError("The tank has reached its maximum capacity of 1000 "
                         "liters and is flooding.")
    print(f"Add {liters} liters to the tank!")


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===\n")
    try:
        print("Testing PlantError...")
        check_plant_height(-1)
    except PlantError as e:
        print("PlantError caught:", e)

    print()

    try:
        print("Testing WaterError...")
        add_water_to_tank(1001)
    except WaterError as e:
        print("WaterError caught:", e)

    print()

    print("Testing catching all garden errors...")
    try:
        check_soil(5)
    except GardenError as e:
        print("GardenError caught:", e)

    try:
        add_water_to_tank(1001)
    except GardenError as e:
        print("GardenError caught:", e)
    print("\nAll custom error types work correctly!\n")
