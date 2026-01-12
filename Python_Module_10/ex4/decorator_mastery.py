from functools import wraps
from datetime import datetime


# Decorator that measures execution time
def spell_timer(func: callable) -> callable:
    @wraps(func)
    def timer(*args, **kwargs):
        print(f"Casting {func.__name__}...")
        start = datetime.now()
        result = func(*args, **kwargs)
        end = datetime.now()
        duration = (end - start).total_seconds()
        print(f"Spell completed in {duration} seconds")
        return result
    return timer


# Decorator factory that validates minimum power
def power_validator(min_power: int) -> callable:
    def decorator(func):
        @wraps(func)
        def check_power(*args, **kwargs):
            power = args[2]  # power is the third argument
            if power < min_power:
                return "Insufficient power for this spell"
            return func(*args, **kwargs)
        return check_power
    return decorator


# Decorator that retries a function if it fails
def retry_spell(max_attempts: int) -> callable:
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    print(f"Spell failed, retrying... "
                          f"(attempt {attempt}/{max_attempts})")
            return f"Spell casting failed after {max_attempts} attempts"
        return wrapper
    return decorator


class MageGuild:
    # Static method to validate mage names
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        return len(name) >= 3 and all(c.isalpha() or c.isspace() for c in name)

    # Decorated spell casting method
    @retry_spell(3)
    @power_validator(10)
    @spell_timer
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with power {power}"


@retry_spell(3)
def test_spell():
    raise RuntimeError("Spell explosion!")


if __name__ == "__main__":

    mage = MageGuild()

    print("\nTesting validate mage name...")
    print("Nome \"Mage\" válido:", MageGuild.validate_mage_name("Mage"))
    print("Nome \"Ma\" válido:", MageGuild.validate_mage_name("Ma"))

    print("\nTesting with valid power...")
    result = mage.cast_spell("iceblast", 20)
    print("Resultado:", result)

    print("\nTesting with invalid power...")
    result = mage.cast_spell("fireball", 5)
    print("Resultado:", result)

    print("\nTesting retry spell...")
    print(test_spell())
