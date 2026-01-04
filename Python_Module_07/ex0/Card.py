from abc import ABC, abstractmethod
from enum import Enum


class CardRarity(Enum):
    Common = 1
    Rare = 2
    Epic = 3
    Legendary = 4


class CardType(Enum):
    Creature = 1
    Spell = 2
    Artifact = 3


class Card(ABC):
    def __init__(self,
                 name: str,
                 cost: int,
                 rarity: CardRarity) -> None:
        self.name = name
        self.cost = cost
        self.rarity = rarity

    @abstractmethod
    def play(self, game_state: dict) -> dict:
        pass

    def get_card_info(self) -> dict:
        card_info = {
            "name": self.name,
            "cost": self.cost,
            "rarity": self.rarity.name,
        }
        return card_info

    def is_playable(self, available_mana: int) -> bool:
        return self.cost <= available_mana
