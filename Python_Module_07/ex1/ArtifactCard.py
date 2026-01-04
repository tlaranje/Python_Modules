from ex0.Card import Card
from ex0.Card import CardRarity, CardType

class ArtifactCard(Card):
    def __init__(self,
            name: str,
            cost: int,
            rarity: CardRarity,
            durability: int,
            effect: str) -> None:
        super().__init__(name, cost, rarity)
        self.durability = durability
        self.effect = effect
        self.type = CardType.Artifact

    def get_card_info(self) -> dict:
        card_info = {
            "name": self.name,
            "cost": self.cost,
            "rarity": self.rarity.name,
            "durability": self.durability,
            "effect": self.effect,
            "type": self.type.name,
        }
        return card_info

    def play(self, game_state: dict) -> dict:
        game_state["card_played"] = self.name
        game_state["mana_used"] = self.cost
        game_state["effect"] = self.effect
        return game_state

    def activate_ability(self) -> dict:
        if self.durability <= 0:
            return {
                "artifact_name": self.name,
                "effect": None,
                "status": "Destroyed"}

        return {
            "artifact_name": self.name,
            "effect": self.effect,
            "status": "Active"}
