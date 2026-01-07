import random
from ex0.Card import Card
from ex0.Card import CardType


class Deck():
    def __init__(self):
        self.deck = []
        self.game_engine = None

    def add_card(self, card: Card) -> None:
        card.deck = self
        self.deck.append(card)

    def remove_card(self, card_name: str) -> bool:
        for c in self.deck:
            if c.name == card_name:
                self.deck.remove(c)
                return True
        return False

    def shuffle(self) -> None:
        random.shuffle(self.deck)

    def draw_card(self) -> Card:
        if not self.deck:
            return None
        return self.deck.pop(0)

    def get_deck_stats(self) -> dict:
        total_cards = len(self.deck)
        creatures = sum(1 for c in self.deck if c.type == CardType.Creature)
        spells = sum(1 for c in self.deck if c.type == CardType.Spell)
        artifacts = sum(1 for c in self.deck if c.type == CardType.Artifact)
        total_cost = sum(c.cost for c in self.deck)

        return {
            "total_cards": total_cards,
            "creatures": creatures,
            "spells": spells,
            "artifacts": artifacts,
            "avg_cost": total_cost / total_cards if total_cards > 0 else 0
        }
