import random
from ex3.CardFactory import CardFactory
from ex0.Card import CardRarity, CardType


class FantasyCardFactory(CardFactory):
    def __init__(self, deck):
        self.deck = deck

    def create_creature(self, name_or_power) -> None:
        from ex0.CreatureCard import CreatureCard
        card = CreatureCard(
            name_or_power,
            random.randint(1, 5),
            random.choice(list(CardRarity)),
            random.randint(1, 10),
            random.randint(1, 10)
        )
        self.deck.add_card(card)

    def create_spell(self, name_or_power) -> None:
        from ex1.SpellCard import SpellCard, EffectType
        card = SpellCard(
            name_or_power,
            random.randint(1, 5),
            random.choice(list(CardRarity)),
            random.choice(list(EffectType))
        )
        self.deck.add_card(card)

    def create_artifact(self, name_or_power) -> None:
        from ex1.ArtifactCard import ArtifactCard, Effects
        card = ArtifactCard(
            name_or_power,
            random.randint(1, 5),
            random.choice(list(CardRarity)),
            random.randint(1, 10),
            random.choice(list(Effects))
        )
        self.deck.add_card(card)

    def create_themed_deck(self, size: int) -> dict:
        deck_info = { "creatures": 0, "spells": 0, "artifacts": 0 }
        creators = [
            self.create_creature,
            self.create_spell,
            self.create_artifact ]

        for _ in range(size):
            creator = random.choice(creators)
            creator(f"Card{random.randint(1, 10)}")
            
            if creator == self.create_creature:
                deck_info["creatures"] += 1
            elif creator == self.create_spell:
                deck_info["spells"] += 1
            elif creator == self.create_artifact:
                deck_info["artifacts"] += 1

        return deck_info

    def get_supported_types(self) -> dict:
        supported = {
            'creatures': [],
            'spells': [],
            'artifacts': []
        }

        for card in self.deck.game_engine.hand:
            if card.type == CardType.Creature:
                supported['creatures'].append(card.name)
            elif card.type == CardType.Spell:
                supported['spells'].append(card.name)
            elif card.type == CardType.Artifact:
                supported['artifacts'].append(card.name)

        return supported
