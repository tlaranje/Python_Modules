import random
from ex2.EliteCard import EliteCard as ECard
from ex1.SpellCard import SpellCard, EffectType
from ex0.Card import CardRarity
from ex1.Deck import Deck


if __name__ == "__main__":
    print("=== DataDeck Ability System ===\n")

    print("EliteCard capabilities:")
    print("- Card: ['play', 'get_card_info', 'is_playable']")
    print("- Combatable: ['attack', 'defend', 'get_combat_stats']")
    print("- Magical: ['cast_spell', 'channel_mana', 'get_magic_stats']\n")

    deck = Deck()
    print("Playing Arcane Warrior (Elite Card):\n")
    Arcane_Warrior = ECard("Arcane_Warrior", 10, CardRarity.Legendary, 4)
    deck.add_card(Arcane_Warrior)
    game_state = {"Name": None, "Cost": 0, "Rarity": None}
    Arcane_Warrior.play(game_state)

    print(f"Combat phase: {Arcane_Warrior.attack("Enemy")}")
    print(f"Defense result: {Arcane_Warrior.defend(random.randint(1, 5))}\n")

    print("Magic phase:")
    spell = SpellCard(
        "Fireball", 4, CardRarity.Common, EffectType.Damage)
    deck.add_card(spell)
    Arcane_Warrior.spells.append(spell)
    print("Spell cast: "
          f"{Arcane_Warrior.cast_spell(spell.name, ["Enemy1", "Enemy2"])}")
    print(f"Mana channel: {Arcane_Warrior.channel_mana(3)}\n")

    print("Multiple interface implementation successful!")
