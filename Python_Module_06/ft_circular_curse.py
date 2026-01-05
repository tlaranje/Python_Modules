
if __name__ == "__main__":
    from alchemy.grimoire.validator import validate_ingredients as vi
    from alchemy.grimoire.spellbook import record_spell as rs

    print("=== Circular Curse Breaking ===\n")

    print("Testing ingredient validation:")
    print(f"validate_ingredients(\"fire air\"): {vi('fire air')}")
    print(f"validate_ingredients(\"dragon scales\"): {vi('dragon scales')}\n")

    print("Testing spell recording with validation:")
    print("record_spell(\"Fireball\", \"fire air\"): "
          f"{rs('Fireball', 'fire air')}")
    print("record_spell(\"Dark Magic\", \"shadow\"): "
          f"{rs('Dark Magic', 'shadow')}\n")

    print("Testing late import technique:")
    print("record_spell(\"Lightning\", \"air\"): "
          f"{rs('Lightning', 'air')}")
    print("Circular dependency curse avoided using late imports!\n")

    print("All spells processed safely!")
