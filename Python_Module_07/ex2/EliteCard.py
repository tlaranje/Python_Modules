import random
from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical


class EliteCard(Card, Combatable, Magical):
    def __init__(self, name, cost, rarity, mana):
        super().__init__(name, cost, rarity)
        self.type = "Elite"
        self.spells = []
        self.mana = mana

    def play(self, game_state: dict) -> dict:
        game_state["Name"] = self.name
        game_state["Cost"] = self.cost
        game_state["Rarity"] = self.rarity
        return game_state

    def get_combat_stats(self) -> dict:
        return {
            "name": self.name,
            "card_type": self.type,
            "combat_style": "melee",
            "damage_range": "1-10",
            "can_attack": True,
            "can_defend": True
        }

    def attack(self, target) -> dict:
        attack_res = {
            "attacker": self.name,
            "target": target,
            "damage": random.randint(1, 10),
            "combat_type": "melee"
        }
        return attack_res

    def defend(self, incoming_damage: int) -> dict:
        defend_res = {
            'defender': self.name,
            'damage_taken': incoming_damage,
            'damage_blocked': random.randint(1, 10),
            'still_alive': True
        }
        if defend_res["damage_taken"] > defend_res["damage_blocked"]:
            defend_res["still_alive"] = False
        return defend_res

    def cast_spell(self, spell_name: str, targets: list) -> dict:
        spell = None
        for s in self.spells:
            if s.name == spell_name:
                spell = s

        if spell is None:
            return {
                "caster": self.name,
                "spell": spell_name,
                "error": "Spell not found"
            }

        spell_res = {
            "caster": self.name,
            "spell": spell_name,
            "targets": targets,
            "mana_used": spell.cost
        }
        return spell_res

    def channel_mana(self, amount: int) -> dict:
        self.mana += amount
        return {
            "channeled": amount,
            "total_mana": self.mana
        }

    def get_magic_stats(self) -> dict:
        return {
            "name": self.name,
            "mana": self.mana,
            "total_spells": len(self.spells),
            "spells": [s.name for s in self.spells]
        }
