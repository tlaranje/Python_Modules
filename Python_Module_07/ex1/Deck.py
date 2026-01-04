import random
from ex0.Card import Card
from ex0.Card import CardType

class Deck():
    def __init__(self):
        self.deck_cards = []
        self.play_cards = []

    def add_card(self, card: Card) -> None:
        self.deck_cards.append(card)

    def remove_card(self, card_name: str) -> bool:
        for c in self.deck_cards:
            if c.name == card_name:
                self.deck_cards.remove(c)
                return True
        return False

    def shuffle(self) -> None:
        random.shuffle(self.deck_cards)

    def draw_card(self) -> Card:
        if not self.deck_cards:
            return None

        card = self.deck_cards[-1]
        self.remove_card(card.name)

        if card.type != CardType.Spell:
            self.play_cards.append(card)

        return card

    def get_deck_stats(self) -> dict:
        total_cards = 0
        creatures = 0
        spells = 0
        artifacts = 0
        total_cost = 0

        for c in self.deck_cards:
            if c.type == CardType.Creature:
                creatures += 1
            elif c.type == CardType.Spell:
                spells += 1
            elif c.type == CardType.Artifact:
                artifacts += 1
            total_cost += c.cost
            total_cards += 1

        deck_stats = {
            "total_cards": total_cards,
            "creatures": creatures,
            "spells": spells,
            "artifacts": artifacts,
            "avg_cost": total_cost / total_cards if total_cards > 0 else 0
        }

        return deck_stats
