from ex0.Card import Card
from ex0.Card import CardRarity, CardType


class CreatureCard(Card):
    def __init__(self,
                 name: str,
                 cost: int,
                 rarity: CardRarity,
                 attack: int,
                 health: int) -> None:
        super().__init__(name, cost, rarity)

        if attack < 0:
            raise ValueError("Attack must be a positive value")
        if health < 0:
            raise ValueError("Health must be a positive value")

        self.type = CardType.Creature
        self.attack = attack
        self.health = health

    def play(self, game_state: dict) -> dict:
        game_state["card_played"] = self.name
        game_state["mana_used"] = self.cost
        game_state["effect"] = "Creature summoned to battlefield"

        return game_state

    def get_card_info(self) -> dict:
        card_info = {
            "name": self.name,
            "cost": self.cost,
            "rarity": self.rarity.name,
            "type": self.type.name,
            "attack": self.attack,
            "health": self.health
        }
        return card_info

    def attack_target(self, target) -> dict:
        combat_resolved = target.health <= self.attack

        return {"attacker": self.name,
                "target": target.name,
                "damage_dealt": self.attack,
                "combat_resolved": combat_resolved}
