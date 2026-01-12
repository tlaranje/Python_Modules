# Sort artifacts by power in descending order using a lambda
def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda x: x["power"], reverse=True)

# Filter mages whose power is greater than or equal to min_power
def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda x: x["power"] >= min_power, mages))

# Add "* " prefix and " *" suffix to each spell name
def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda x: "* " + x + " *", spells))

# Calculate max, min, and average power of mages
def mage_stats(mages: list[dict]) -> dict:
    max_power = max(mages, key=lambda x: x["power"])["power"]
    min_power = min(mages, key=lambda x: x["power"])["power"]
    avg_power = round(sum(map(lambda x: x["power"], mages)) / len(mages), 2)
    return {
        'max_power': max_power,
        'min_power': min_power,
        'avg_power': avg_power}


if __name__ == "__main__":
    artifacts = [
        {'name': 'Water Chalice', 'power': 60, 'type': 'accessory'},
        {'name': 'Earth Shield', 'power': 74, 'type': 'relic'},
        {'name': 'Shadow Blade', 'power': 95, 'type': 'weapon'},
        {'name': 'Fire Staff', 'power': 85, 'type': 'focus'}]

    mages = [
        {'name': 'Morgan', 'power': 83, 'element': 'light'},
        {'name': 'Casey', 'power': 94, 'element': 'light'},
        {'name': 'Ember', 'power': 72, 'element': 'earth'},
        {'name': 'Zara', 'power': 75, 'element': 'earth'},
        {'name': 'Kai', 'power': 63, 'element': 'light'}]

    spells = ['heal', 'meteor', 'freeze', 'lightning']

    print("\nTesting artifact sorter:")
    print("+-------+---------------+-------+-----------+")
    print("| Index | Name          | Power | Type      |")
    print("+-------+---------------+-------+-----------+")

    for i, a in enumerate(artifact_sorter(artifacts), start=0):
        print(f"| {i:<6}|"
              f" {a['name']:<13} |"
              f" {a['power']:<5} |"
              f" {a['type']:<9} |")

    print("+-------+---------------+-------+-----------+")

    print("\nTesting power filter (>=73):")
    for m in power_filter(mages, 73):
        print(f"- {m['name']} ({m['power']} power, {m['element']} element)")

    print("\nTesting spell transformer:")
    for s in spell_transformer(spells):
        print(f"- {s}")

    print("\nTesting mage stats:")
    m = mage_stats(mages)
    print(f"Max_power: {m['max_power']}")
    print(f"Min_power: {m['min_power']}")
    print(f"Avg_power: {m['avg_power']}")
