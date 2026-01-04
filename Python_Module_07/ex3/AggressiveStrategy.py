import random
from ex3.GameStrategy import GameStrategy
from ex0.Card import CardType, CardRarity
from ex0.CreatureCard import CreatureCard


class AggressiveStrategy(GameStrategy):
    def execute_turn(self, hand: list, battlefield: list) -> dict:
        cards_played = []
        mana_used = 0
        targets_attacked = []
        damage_dealt = 0

        for card in hand:
            game_state = card.play({
                "card_played": None,
                "mana_used": 0,
                "effect": None})

            enemy = CreatureCard("Enemy Player", 5, CardRarity.Common, 1, 5)

            mana_used += game_state["mana_used"]
            cards_played.append(card.name)

            if card.type == CardType.Creature:
                battlefield.append(card)
                dmg = card.attack_target(enemy)
                damage_dealt += dmg["damage_dealt"]
                targets_attacked.append(enemy.name)
            elif card.type == CardType.Spell:
                damage_dealt += random.randint(1, 5)
            elif card.type == CardType.Artifact:
                battlefield.append(card)

            hand.remove(card)

        return {
            "cards_played": cards_played,
            "mana_used": mana_used,
            "targets_attacked": targets_attacked,
            "damage_dealt": damage_dealt
        }

    def get_strategy_name(self) -> str:
        return "AggressiveStrategy"

    def prioritize_targets(self, available_targets: list) -> list:
        if not available_targets:
            return []
        return available_targets
