
def record_spell(spell_name: str, ingredients: str) -> str:
    from .validator import validate_ingredients
    is_valid = validate_ingredients(ingredients)

    if is_valid.split("-")[1].strip() == "VALID":
        return f"Spell recorded: {spell_name} ({is_valid})"
    else:
        return f"Spell recorded: {spell_name} ({is_valid})"
