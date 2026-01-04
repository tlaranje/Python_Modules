from ex1.Deck import Deck
from ex0.CreatureCard import CreatureCard as CCard
from ex1.ArtifactCard import ArtifactCard as ACard
from ex1.SpellCard import SpellCard as SCard
from ex0.Card import CardRarity
from ex1.SpellCard import EffectType


if __name__ == "__main__":
    print("=== DataDeck Deck Builder ===\n")

    print("Building deck with different card types...")

    deck = Deck()
    creature = CCard(
        "Fire Dragon", 4, CardRarity.Legendary, 7, 5)
    spell = SCard(
        "Lightning Bolt", 4, CardRarity.Common, EffectType.Damage)
    artifact = ACard(
        "Mana Crystal", 4, CardRarity.Common, 5, "Permanent: +1 mana per turn")
    deck.add_card(creature)
    deck.add_card(artifact)
    deck.add_card(spell)
    print(f"Deck stats: {deck.get_deck_stats()}\n")

    print("Drawing and playing cards:\n")

    while deck.deck_cards:
        c = deck.draw_card()
        print(f"Drew: {c.name} ({c.get_card_info()["type"]})")
        game_state =  {'card_played': None, 'mana_used': 0, 'effect': None}
        print(f"Play result: {c.play(game_state)}\n")

    print("Polymorphism in action: Same interface, different card behaviors!")

"""
=== DataDeck Deck Builder ===

Building deck with different card types...
Deck stats: {'total_cards': 3, 'creatures': 1, 'spells': 1,'artifacts': 1, 'avg_cost': 4.0}

Drawing and playing cards:

Drew: Lightning Bolt (Spell)
Play result: {'card_played': 'Lightning Bolt', 'mana_used': 3,
'effect': 'Deal 3 damage to target'}

Drew: Mana Crystal (Artifact)
Play result: {'card_played': 'Mana Crystal', 'mana_used': 2,
'effect': 'Permanent: +1 mana per turn'}

Drew: Fire Dragon (Creature)
Play result: {'card_played': 'Fire Dragon', 'mana_used': 5,
'effect': 'Creature summoned to battlefield'}

Polymorphism in action: Same interface, different card behaviors!
 """
