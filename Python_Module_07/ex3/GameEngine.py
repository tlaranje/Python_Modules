from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy


class GameEngine:
    def __init__(self, deck):
        self.deck = deck
        self.hand = []
        self.battlefield = []
        self.deck.game_engine = self
        self.strategy = None

    def configure_engine(
            self, factory: CardFactory, strategy: GameStrategy) -> None:
        self.strategy = strategy

        cards_to_create = [
            ("creature", "Fire Dragon"),
            ("creature", "Goblin Warrior"),
            ("spell", "Lightning Bolt"),
            ("artifact", "Mana Ring")]

        for card_type, name in cards_to_create:
            if card_type == "creature":
                factory.create_creature(name)
            elif card_type == "spell":
                factory.create_spell(name)
            elif card_type == "artifact":
                factory.create_artifact(name)

        self.deck.shuffle()

        if len(self.deck.deck) == 0:
            raise RuntimeError("Factory did not add any cards to the deck")

        for _ in range(3):
            if self.deck.deck:
                self.hand.append(self.deck.draw_card())

    def simulate_turn(self) -> dict:
        if not self.strategy:
            raise RuntimeError("Strategy not configured")

        return self.strategy.execute_turn(self.hand, self.battlefield)

    def get_engine_status(self) -> dict:
        return {
            "deck_size": len(self.deck.deck),
            "hand": [card.name for card in self.hand],
            "battlefield": [card.name for card in self.battlefield]
        }
