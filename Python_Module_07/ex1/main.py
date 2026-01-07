from ex1.Deck import Deck
from ex0.CreatureCard import CreatureCard
from ex1.ArtifactCard import ArtifactCard, Effects
from ex1.SpellCard import SpellCard, EffectType
from ex0.Card import CardRarity


if __name__ == "__main__":
    print("=== DataDeck Deck Builder ===\n")

    try:
        deck = Deck()

        creature = CreatureCard(
            "Fire Dragon", 4, CardRarity.Legendary, 7, 5)
        spell = SpellCard(
            "Lightning Bolt", 4, CardRarity.Common, EffectType.Damage)
        artifact = ArtifactCard(
            "Mana Crystal", 4, CardRarity.Common, 5, Effects.PERMANENT_MANA)

        print("Building deck with different card types...")

        deck.add_card(creature)
        deck.add_card(artifact)
        deck.add_card(spell)

        print(f"Deck stats: {deck.get_deck_stats()}\n")
        print("Drawing and playing cards:\n")

        while deck.deck:
            c = deck.draw_card()
            print(f"Drew: {c.name} ({c.get_card_info()['type']})")
            game_state = {'card_played': None, 'mana_used': 0, 'effect': None}
            print(f"Play result: {c.play(game_state)}\n")

        print("Polymorphism in action: Same interface, "
              "different card behaviors!")
    except Exception as e:
        print(f"Error: {e}")
