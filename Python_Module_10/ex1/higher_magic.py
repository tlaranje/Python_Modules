# Basic example spells
def fireball(damage: int) -> int:
    return damage


def heal(healing: int) -> int:
    return healing


def check_power(power: int) -> bool:
    return power > 5

# Combine two spells and return both results as a tuple
def spell_combiner(spell1: callable, spell2: callable) -> callable:
    return lambda *x: (spell1(*x), spell2(*x))

# Amplify the result of a spell by a multiplier
def power_amplifier(base_spell: callable, multiplier: int) -> callable:
    return lambda *x: base_spell(*x) * multiplier

# Cast a spell only if the condition is True
def conditional_caster(condition: callable, spell: callable) -> callable:
    return lambda *x: spell(*x) if condition(*x) else "Spell fizzled"

# Cast a list of spells in sequence and return all results
def spell_sequence(spells: list[callable]) -> callable:
    return lambda *x: [spell(*x) for spell in spells]


if __name__ == "__main__":
    damage = 10

    combiner = spell_combiner(fireball, heal)
    print("Testing spell_combiner:")
    print(f"Combined spell result: {combiner(damage)}\n")

    amplifier = power_amplifier(fireball, 2)
    print("Testing power_amplifier:")
    print(f"Original: {damage}, Amplified: {amplifier(damage)}\n")

    caster = conditional_caster(check_power, fireball)
    print("Testing conditional_caster:")
    print(f"{caster(damage)}\n")

    spells = [fireball, heal]
    sequence = spell_sequence(spells)
    print("Testing spell_sequence:")
    print(f"{sequence(damage)}")
