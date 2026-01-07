import random
from ex0.Card import Card
from ex0.Card import CardRarity, CardType
from enum import Enum


class Effects(Enum):
    PERMANENT_MANA = "mana"
    PERMANENT_HEALTH = "health"
    PERMANENT_ATTACK = "attack"


class ArtifactCard(Card):
    def __init__(self,
                 name: str,
                 cost: int,
                 rarity: CardRarity,
                 durability: int,
                 effect: Effects,) -> None:
        super().__init__(name, cost, rarity)

        if durability <= 0:
            raise ValueError("Durability must be a positive value")

        self.durability = durability
        self.effect = effect
        self.value = random.randint(1, 5)
        self.type = CardType.Artifact

    def get_card_info(self) -> dict:
        card_info = {
            "name": self.name,
            "cost": self.cost,
            "rarity": self.rarity.name,
            "durability": self.durability,
            "effect": f"Permanent: +{self.value} {self.effect.value} per turn",
            "type": self.type.name,
        }
        return card_info

    def play(self, game_state: dict) -> dict:
        game_state["card_played"] = self.name
        game_state["mana_used"] = self.cost
        game_state["effect"] = (
            f"Permanent: +{self.value} {self.effect.value} per turn")

        return game_state

    def activate_ability(self) -> dict:
        if self.durability <= 0:
            return {
                "artifact_name": self.name,
                "effect": None,
                "status": "Destroyed"}

        self.durability -= 1

        return {
            "artifact_name": self.name,
            "effect": f"Permanent: +{self.value} {self.effect.value} per turn",
            "status": "Active"}
