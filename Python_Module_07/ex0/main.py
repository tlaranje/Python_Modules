from ex0.CreatureCard import CreatureCard as CCard
from ex0.CreatureCard import CardRarity as CRarity

if __name__ == "__main__":
    print("=== DataDeck Card Foundation ===\n")

    print("Testing Abstract Base Class Design:")
    print("CreatureCard Info:")
    dragon = CCard("Fire Dragon", 5, CRarity.Legendary, 7, 5)
    print(f"{dragon.get_card_info()}\n")

    print("Playing Fire Dragon with 6 mana available:")
    print(f"Playable: {dragon.is_playable(6)}")
    game_state =  {'card_played': None, 'mana_used': 0, 'effect': None}
    print(f"Play result: {dragon.play(game_state)}\n")

    print("Fire Dragon attacks Goblin Warrior:")
    goblin = CCard("Goblin Warrior", 5, CRarity.Common, 2, 5)
    print(f"Attack result: {dragon.attack_target(goblin)}\n")

    print("Testing insufficient mana (3 available):")
    print(f"Playable: {dragon.is_playable(3)}\n")

    print("Abstract pattern successfully demonstrated!")