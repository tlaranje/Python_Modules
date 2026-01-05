from ex0.Card import Card, CardRarity
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):
    def __init__(self,
                 name: str,
                 cost: int,
                 rarity: CardRarity,
                 attack_power: int,
                 health: int,
                 rating: int,
                 card_id: str) -> None:
        super().__init__(name, cost, rarity)
        self.attack_power = attack_power
        self.health = health
        self.rating = rating
        self.card_id = card_id
        self.wins = 0
        self.losses = 0

    def play(self, game_state: dict) -> dict:
        return self.attack(game_state["opponent"])

    def attack(self, target) -> dict:
        return target.defend(self.attack_power)

    def defend(self, incoming_damage: int) -> dict:
        remaining_health = self.health - incoming_damage
        return {
            "damage_taken": incoming_damage,
            "remaining_health": remaining_health
        }

    def get_tournament_stats(self) -> dict:
        return {"card_id": self.card_id,
                "name": self.name,
                "rating": self.rating,
                "wins": self.wins,
                "losses": self.losses,
                "attack_power": self.attack_power,
                "health": self.health}

    def get_combat_stats(self) -> dict:
        return {"attack_power": self.attack_power,
                "health": self.health}

    def get_rank_info(self) -> dict:
        return {"rating": self.rating,
                "wins": self.wins,
                "losses": self.losses}

    def calculate_rating(self) -> int:
        return self.rating

    def update_wins(self, wins: int) -> None:
        self.wins += wins

    def update_losses(self, losses: int) -> None:
        self.losses += losses
