import random
from enum import Enum
from ex0.Card import Card
from ex0.Card import CardRarity, CardType


class EffectType(Enum):
    Damage = 1
    Heal = 2
    Buff = 3
    Debuff = 4


class SpellCard(Card):
    def __init__(self,
            name: str,
            cost: int,
            rarity: CardRarity,
            effect_type: EffectType) -> None:
        super().__init__(name, cost, rarity)
        self.effect_type = effect_type
        self.type = CardType.Spell

    def get_card_info(self) -> dict:
        card_info = {
            "name": self.name,
            "cost": self.cost,
            "rarity": self.rarity.name,
            "effect_type": self.effect_type.name,
            "type": self.type.name,
        }
        return card_info

    def play(self, game_state: dict) -> dict:
        game_state["card_played"] = self.name
        game_state["mana_used"] = self.cost

        effect = self.resolve_effect(["Enemy"])

        if effect["type"] == EffectType.Damage:
            game_state["effect"] = f"Deal {effect['value']} damage to target"
        elif effect["type"] == EffectType.Heal:
            game_state["effect"] = f"Heal {effect['value']} health to target"
        elif effect["type"] == EffectType.Buff:
            game_state["effect"] = (
                f"Buff target with +{effect['value']} health "
                f"for {effect['duration']} turns")
        elif effect["type"] == EffectType.Debuff:
            game_state["effect"] = (
                f"Debuff target with -{effect['value']} health "
                f"for {effect['duration']} turns")

        return game_state

    def resolve_effect(self, targets: list) -> dict:
        effect = {
            "type": self.effect_type,
            "value": 0,
            "duration": None,
            "target": targets
        }

        if not targets:
            return effect

        if self.effect_type == EffectType.Damage:
            effect["value"] = random.randint(1, 5)
        elif self.effect_type == EffectType.Heal:
            effect["value"] = random.randint(1, 5)
        elif self.effect_type == EffectType.Buff:
            effect["value"] = random.randint(1, 3)
            effect["duration"] = random.randint(1, 3)
        elif self.effect_type == EffectType.Debuff:
            effect["value"] = random.randint(1, 3)
            effect["duration"] = random.randint(1, 3)

        return effect
