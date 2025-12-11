
def check_temperature(temp_str):
    """Check if the given tmp_str is valid and within 0-40°C for plants."""
    try:
        print(f"Testing temperature: {temp_str}")
        temp = int(temp_str)
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number\n")
        return

    if 0 < temp <= 40:
        print(f"Temperature {temp}°C is perfect for plants!\n")
        return temp
    elif temp > 40:
        print(f"Error: {temp}°C is too hot for plants (max 40°C)\n")
    elif temp < 0:
        print(f"Error: {temp}°C is too cold for plants (min 0°C)\n")


def test_temperature_input():
    """Run basic tests for the check_temperature function."""
    print("=== Garden Temperature Checker ===\n")
    check_temperature("25")
    check_temperature("abc")
    check_temperature("100")
    check_temperature("-50")
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature_input()
