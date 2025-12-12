
def water_plants(plant_list):
    """Water each plant in the list and handle invalid plant entries."""
    print("Opening watering system")

    try:
        for plant in plant_list:
            plant[0]
            print(f"Watering {plant}")
    except Exception:
        print(f"Cannot water {plant} - invalid plant")
        return
    finally:
        print("Closing watering system (cleanup)")

    print("Watering completed successfully!")


def test_watering_system():
    print("=== Garden Watering System ===\n")

    print("Testing normal watering...")
    water_plants(["Tomato", "Lettuce", "Carrots"])

    print("\nTesting with error...")
    water_plants(["Tomato", None, "Carrots"])

    print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
