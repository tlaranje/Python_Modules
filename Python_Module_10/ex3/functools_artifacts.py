from functools import reduce, partial, lru_cache, singledispatch
from operator import add, mul

# Example spells
def fireball(damage: int) -> int:
    return damage


def heal(healing: int) -> int:
    return healing


# Reduce spell powers using different operations
def spell_reducer(spells: list[int], operation: str) -> int:
    ops = {"add": add, "multiply": mul, "max": max, "min": min}
    func = ops[operation]

    # max and min need a lambda because operator.max/min don't exist
    if operation in ("max", "min"):
        return reduce(lambda x, y: func(x, y), spells)

    return reduce(func, spells)


# Example base enchantment function
def base_ench(power: int, element: str, target: str) -> str:
    return f"Power: {power}, Element: {element}, Target: {target}"


# Create partial enchantment functions with fixed power and element
def partial_enchanter(base_enchantment: callable) -> dict[str, callable]:
    return {
        "fire_enchant": partial(base_enchantment, 50, "fire"),
        "ice_enchant": partial(base_enchantment, 50, "ice"),
        "lightning_enchant": partial(base_enchantment, 50, "lightning")
    }


# Memoized Fibonacci using LRU cache
@lru_cache(maxsize=128)
def memoized_fibonacci(n: int) -> int:
    if n < 2:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


# Single-dispatch spell handler
def spell_dispatcher() -> callable:
    @singledispatch
    def cast(spell):
        return "Unknown spell type"

    # Handle integer spells (damage)
    @cast.register
    def _(dmg: int):
        return f"Spell deal {dmg} damage to target"

    # Handle string spells (enchantments)
    @cast.register
    def _(ench: str):
        return f"Enchantment applied: {ench}"

    # Handle list spells (multi-cast)
    @cast.register
    def _(spells: list):
        return [cast(s) for s in spells]

    return cast


if __name__ == "__main__":
    spell_powers = [10, 10, 10, 10, 10]
    operations = ['add', 'multiply', 'max', 'min']

    print("Testing spell reducer...")
    for o in operations:
        reducer = spell_reducer(spell_powers, o)
        print(f"{o}: {reducer}")

    print("\nTesting partial enchanter...")
    enchanter = partial_enchanter(base_ench)
    print(enchanter["fire_enchant"]("sword"))
    print(enchanter["ice_enchant"]("shield"))
    print(enchanter["lightning_enchant"]("staff"))

    print("\nTesting memoized fibonacci...")
    print(f"{memoized_fibonacci(10)}")

    print("\nTesting spell dispatcher...")
    dispatcher = spell_dispatcher()
    print(dispatcher(30))
    print(dispatcher("Flaming Staff"))
    print(dispatcher([5, "Ice Shield", 12]))
