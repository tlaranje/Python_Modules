from ex4.TournamentCard import TournamentCard
from operator import attrgetter


class TournamentPlatform:
    def __init__(self):
        self.r_cards = []
        self.matches_played = 0

    def register_card(self, card: TournamentCard) -> str:
        self.r_cards.append(card)

        return (f"{card.name} (ID: {card.card_id}):\n"
                f"- Interfaces: [Card, Combatable, Rankable]\n"
                f"- Rating: {card.rating}\n"
                f"- Record: {card.wins}-{card.losses}\n")

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        self.matches_played += 1
        card1 = next((c for c in self.r_cards if c.card_id == card1_id), None)
        card2 = next((c for c in self.r_cards if c.card_id == card2_id), None)

        res1 = card1.play({"opponent": card2})
        res2 = card2.play({"opponent": card1})

        if res1["remaining_health"] > res2["remaining_health"]:
            winner, loser = card1, card2
        else:
            winner, loser = card2, card1

        winner.rating += 16
        loser.rating -= 16

        winner.update_wins(1)
        loser.update_losses(1)

        return {
            "winner": winner.card_id,
            "loser": loser.card_id,
            "winner_rating": winner.rating,
            "loser_rating": loser.rating
        }

    def get_leaderboard(self) -> list:
        return [
            {
                "card_id": c.card_id,
                "name": c.name,
                "rating": c.rating,
                "wins": c.wins,
                "losses": c.losses
            }
            for c in sorted(self.res_cards, key=attrgetter("rating"))]

    def generate_tournament_report(self) -> dict:
        total_cards = len(self.r_cards)
        avg_rating = (
            sum(card.rating for card in self.r_cards) / total_cards
            if total_cards > 0 else 0
        )
        return {"total_cards": total_cards,
                "matches_played": self.matches_played,
                "avg_rating": int(avg_rating),
                "platform_status": "active" if total_cards > 0 else "inactive"}
