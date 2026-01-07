from ex0.CreatureCard import CreatureCard
from ex0.Card import CardRarity


if __name__ == "__main__":
    print("=== DataDeck Card Foundation ===\n")

    try:
        dragon = CreatureCard("Fire Dragon", 5, CardRarity.Legendary, 7, 5)
        goblin = CreatureCard("Goblin Warrior", 5, CardRarity.Common, 2, 5)

        print("Testing Abstract Base Class Design:\n")
        print("CreatureCard Info:")
        print(f"{dragon.get_card_info()}\n")

        print("Playing Fire Dragon with 6 mana available:")
        print(f"Playable: {dragon.is_playable(6)}")
        game_state = {'card_played': None, 'mana_used': 0, 'effect': None}
        print(f"Play result: {dragon.play(game_state)}\n")

        print("Fire Dragon attacks Goblin Warrior:")
        print(f"Attack result: {dragon.attack_target(goblin)}\n")

        print("Testing insufficient mana (3 available):")
        print(f"Playable: {dragon.is_playable(3)}\n")

        print("Abstract pattern successfully demonstrated!")
    except Exception as e:
        print(f"Error: {e}")
