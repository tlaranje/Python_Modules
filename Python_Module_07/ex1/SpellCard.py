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
        self.deck = None

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

        eff_types = {
             EffectType.Damage: "Deal {value} damage to target",
             EffectType.Heal: "Heal {value} health to target",
             EffectType.Buff: "Buff target with +{value} health for "
                              "{duration} turns",
             EffectType.Debuff: "Debuff target with -{value} health "
                                "for {duration} turns"}

        eff = eff_types.get(effect["type"], "Unknown effect")

        game_state["effect"] = eff.format(value=effect["value"],
                                          duration=effect["duration"])

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
