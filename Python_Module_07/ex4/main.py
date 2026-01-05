import random
from ex4.TournamentCard import TournamentCard as t_card
from ex4.TournamentPlatform import TournamentPlatform
from ex0.Card import CardRarity


if __name__ == "__main__":
    print("=== DataDeck Tournament Platform ===\n")
    print("Registering Tournament Cards...\n")

    t_platform = TournamentPlatform()

    card1 = t_card("Fire Dragon",
                   random.randint(1, 5),
                   CardRarity.Legendary,
                   random.randint(1, 10),
                   random.randint(1, 10),
                   1200,
                   "dragon_001")

    card2 = t_card("Ice Wizard",
                   random.randint(1, 5),
                   CardRarity.Legendary,
                   random.randint(1, 10),
                   random.randint(1, 10),
                   1150,
                   "wizard_001")

    print(f"{t_platform.register_card(card1)}")
    print(f"{t_platform.register_card(card2)}")

    print("Creating tournament match...")
    print("Match result: "
          f"{t_platform.create_match(card1.card_id, card2.card_id)}\n")

    print("Tournament Leaderboard:")
    print(f"1. {card1.name} - "
          f"Rating: {card1.rating} ({card1.wins}-{card1.losses})")
    print(f"1. {card2.name} - "
          f"Rating: {card2.rating} ({card2.wins}-{card2.losses})\n")

    print("Platform Report:")
    print(t_platform.generate_tournament_report())

    print("\n=== Tournament Platform Successfully Deployed! ===")
    print("All abstract patterns working together harmoniously!")
