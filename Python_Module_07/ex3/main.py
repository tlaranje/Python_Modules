from ex1.Deck import Deck
from ex3.AggressiveStrategy import AggressiveStrategy
from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.GameEngine import GameEngine

if __name__ == "__main__":
    print("=== DataDeck Game Engine ===\n")

    deck = Deck()
    strategy = AggressiveStrategy()
    factory = FantasyCardFactory(deck)
    engine = GameEngine(deck)

    print("Configuring Fantasy Card Game...")
    print("Factory: FantasyCardFactory")
    print("Strategy: AggressiveStrategy")

    engine.configure_engine(factory, strategy)

    print(f"Available types: {factory.get_supported_types()}\n")

    print("Simulating aggressive turn...")
    print(f"Hand: {[f'{c.name} ({c.cost})' for c in engine.hand]}\n")

    print("Turn execution:")
    print(f"Strategy: {strategy.get_strategy_name()}")

    cards_created = (len(factory.get_supported_types()["creatures"])
                     + len(factory.get_supported_types()["spells"])
                     + len(factory.get_supported_types()["artifacts"]))
    actions = strategy.execute_turn(engine.hand, engine.battlefield)

    print(f"Actions: {actions}\n")

    game_report = {
        "turns_simulated": 1,
        "strategy_used": strategy.get_strategy_name(),
        "total_damage": actions.get("damage_dealt", 0),
        "cards_created": cards_created
    }

    print("Game Report:")
    print(game_report)
    print("\nAbstract Factory + Strategy Pattern: "
          "Maximum flexibility achieved!")
