# Closure that counts how many times it has been called
def mage_counter() -> callable:
    count = 0

    def counter() -> int:
        nonlocal count
        count += 1
        return count
    return counter


# Closure that accumulates power over time
def spell_accumulator(initial_power: int) -> callable:
    total_power = initial_power

    def add(x: int) -> int:
        nonlocal total_power
        total_power += x
        return total_power
    return add


# Factory that creates enchantment functions
def enchantment_factory(enchantment_type: str) -> callable:
    return lambda x: enchantment_type + " " + x


# Memory vault using closure to store and recall values
def memory_vault() -> dict[str, callable]:
    mem_stored = {}

    def store(key, value) -> None:
        mem_stored[key] = value

    def recall(key) -> dict:
        return mem_stored.get(key, "Memory not found")

    return {"store": store, "recall": recall}


if __name__ == "__main__":
    print("Testing mage counter...")
    counter = mage_counter()
    for i, _ in enumerate(range(3), start=1):
        print(f"Call {i}: {counter()}")

    print("\nTesting spell accumulator...")
    accumulator = spell_accumulator(0)
    for i, _ in enumerate(range(3), start=1):
        print(f"Call {i}: {accumulator(3)}")

    print("\nTesting enchantment factory...")
    ench_types = ['Frozen', 'Flaming', 'Flowing']
    items = ['Cloak', 'Sword', 'Staff', 'Ring']
    for ench, item in zip(ench_types, items):
        factory = enchantment_factory(ench)
        print(f"{factory(item)}")

    print("\nTesting memory vault...")
    vault = memory_vault()
    vault["store"]("spell", "Fireball")
    vault["store"]("power", 42)
    print(vault["recall"]("spell"))
    print(vault["recall"]("power"))
    print(vault["recall"]("mana"))
