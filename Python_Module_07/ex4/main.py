import random
from ex4.TournamentCard import TournamentCard as t_card
from ex4.TournamentPlatform import TournamentPlatform
from ex0.Card import CardRarity


if __name__ == "__main__":
    print("=== DataDeck Tournament Platform ===\n")
    print("Registering Tournament Cards...\n")

    try:
        t_platform = TournamentPlatform()

        card1 = t_card(
            "Fire Dragon",
            random.randint(1, 5),
            CardRarity.Legendary,
            random.randint(1, 10),
            random.randint(1, 10),
            1200,
            "dragon_001")

        card2 = t_card(
            "Ice Wizard",
            random.randint(1, 5),
            CardRarity.Legendary,
            random.randint(1, 10),
            random.randint(1, 10),
            1150,
            "wizard_001")

        print(f"{t_platform.register_card(card1)}")
        print(f"{t_platform.register_card(card2)}")

        print("Creating tournament match...")
        result = t_platform.create_match(card1.card_id, card2.card_id)
        print(f"Match result: {result}\n")

        print("Tournament Leaderboard:")
        for pos, entry in enumerate(t_platform.get_leaderboard(), start=1):
            print(f"{pos}. {entry['name']} - Rating: {entry['rating']} "
                  f"({entry['wins']}-{entry['losses']})")

        print("\nPlatform Report:")
        print(t_platform.generate_tournament_report())

        print("\n=== Tournament Platform Successfully Deployed! ===")
        print("All abstract patterns working together harmoniously!")

    except Exception as e:
        print(f"Error: {e}")
