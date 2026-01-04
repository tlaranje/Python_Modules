from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy
from ex0.Card import CardType


class GameEngine:
    def __init__(self, deck):
        self.deck = deck
        self.hand = []
        self.battlefield = []
        self.deck.game_engine = self

    def configure_engine(
            self, factory: CardFactory, strategy: GameStrategy) -> None:
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

            while self.deck.deck:
                card = self.deck.draw_card()
                self.hand.append(card)

        self.deck.shuffle()

    def simulate_turn(self) -> dict:
        turn_log = {
            "played_cards": [],
            "battlefield": []
        }

        for card in self.hand[:]:
            turn_log["played_cards"].append(card.name)

            if card.type != CardType.Spell:
                self.battlefield.append(card)
                turn_log["battlefield"].append(card.name)

            self.hand.remove(card)

        return turn_log

    def get_engine_status(self) -> dict:
        return {
            "deck_size": len(self.deck.deck),
            "hand": [card.name for card in self.hand],
            "battlefield": [card.name for card in self.battlefield]
        }
