from functools import wraps
from datetime import datetime


def spell_timer(func: callable) -> callable:
    @wraps(func)
    def timer(*args, **kwargs):
        print(f"Casting {args[1]}...")
        start = datetime.now()
        result = func(*args, **kwargs)
        end = datetime.now()
        duration = (end - start).total_seconds()
        print(f"Spell completed in {duration} seconds")
        return result
    return timer


def power_validator(min_power: int) -> callable:
    def decorator(func):
        @wraps(func)
        def check_power(*args, **kwargs):
            if args[2] < min_power:
                raise ValueError("Insufficient power for this spell")
            return func(*args, **kwargs)
        return check_power
    return decorator


def retry_spell(max_attempts: int) -> callable:
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    print(f"Spell failed, retrying... (attempt {attempt}/"
                          f"{max_attempts})")
            return f"Spell casting failed after {max_attempts} attempts"
        return wrapper
    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        return len(name) >= 3 and all(c.isalpha() or c.isspace() for c in name)

    @retry_spell(3)
    @spell_timer
    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with power {power}"


if __name__ == "__main__":

    mage = MageGuild()

    print("\nTesting validate mage name...")
    print("Nome \"Mage\" válido:", MageGuild.validate_mage_name("Mage"))
    print("Nome \"Ma\" válido:", MageGuild.validate_mage_name("Ma"))

    print("\nTesting with invalid power...")
    try:
        result = mage.cast_spell("fireball", 5)
        print("Resultado:", result)
    except Exception as e:
        print("Erro capturado:", e)

    print("\nTesting with valid power...")
    result = mage.cast_spell("iceblast", 20)
    print("Resultado:", result)
