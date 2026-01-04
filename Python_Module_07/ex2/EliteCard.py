import random
from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical
from ex1.Deck import Deck

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
        pass

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

        spell_res = {
            "caster": self.name,
            "spell": spell_name,
            "targets": targets,
            "mana_used": spell.cost
        }
        return spell_res

    def channel_mana(self, amount: int) -> dict:
        channel_res = {"channeled": amount, "total_mana": amount + self.mana}
        return channel_res
    def get_magic_stats(self) -> dict:
        pass