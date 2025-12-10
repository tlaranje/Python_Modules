
class GardenManager:
    _gardens = []

    def __init__(self, name):
        GardenManager._gardens.append(self)
        self.stats = GardenManager.GardenStats(self)
        self.name = name
        self.plants = []

    def add_plant(self, plant):
        self.plants.append(plant)

    def grow_plants(self, grow):
        print(f"{self.name} is helping all plants grow...")
        total_grow = 0
        for p in self.plants:
            print(f"{p.name} grew {grow}cm")
            p.height += grow
            total_grow += 1
        return total_grow

    @classmethod
    def total_gardens(cls):
        total = 0
        for _ in cls._gardens:
            total += 1
        return total

    @classmethod
    def create_garden_network(cls):
        scores = {}
        for g in cls._gardens:
            score = 0
            for p in g.plants:
                score += p.height
                if p.plant_type == "Prize":
                    score += p.prize * 4
            scores[g.name] = score
        return scores

    @staticmethod
    def validate_heights(garden):
        for p in garden.plants:
            if p.height < 0:
                return False
        return True

    class GardenStats:
        def __init__(self, garden):
            self.garden = garden

        def count_by_type(self):
            counts = {"regular": 0, "flowering": 0, "prize": 0}
            for plant in self.garden.plants:
                if (plant.plant_type == "Regular"):
                    counts["regular"] += 1
                elif (plant.plant_type == "Flowering"):
                    counts["flowering"] += 1
                elif (plant.plant_type == "Prize"):
                    counts["prize"] += 1
            return counts

        def garden_report(self):
            total_grow = self.garden.grow_plants(1)
            print(f"\n=== {self.garden.name}'s Garden Report ===")
            print("Plants in garden:")
            total_plant = 0
            for plant in self.garden.plants:
                if (plant.plant_type == "Regular"):
                    print(f"- {plant.name}: {plant.height}cm")
                elif (plant.plant_type == "Flowering"):
                    print(
                        f"- {plant.name}: {plant.height}cm, "
                        f"{plant.color} flowers (blooming)")
                elif (plant.plant_type == "Prize"):
                    print(
                        f"- {plant.name}: {plant.height}cm, "
                        f"{plant.color} flowers (blooming), "
                        f"Prize points: {plant.prize}")
                total_plant += 1
            counts = self.count_by_type()
            print(f"\nPlants added: {total_plant}, Total growth: {total_grow}")
            print(f"Plant types: {counts['regular']} regular, "
                  f"{counts['flowering']} flowering, "
                  f"{counts['prize']} prize flowers")


class Plant:
    def __init__(self, plant_type, name, height):
        self.plant_type = plant_type
        self.name = name
        self.height = height


class FloweringPlant(Plant):
    def __init__(self, plant_type, name, height, color):
        super().__init__(plant_type, name, height)
        self.color = color


class PrizeFlower(FloweringPlant):
    def __init__(self, plant_type, name, height, color, prize):
        super().__init__(plant_type, name, height, color)
        self.prize = prize


if __name__ == "__main__":
    print("=== Garden Management System Demo ===\n")

    alice = GardenManager("Alice")
    alice.add_plant(Plant("Regular", "Oak Tree", 100))
    alice.add_plant(FloweringPlant("Flowering", "Rose", 25, "red"))
    alice.add_plant(PrizeFlower("Prize", "Sunflower", 50, "yellow", 10))

    for p in alice.plants:
        print(f"Added {p.name} to {alice.name}'s garden")
    print()

    alice.stats.garden_report()

    bob = GardenManager("Bob")
    bob.add_plant(Plant("Regular", "Pine Tree", 40))
    bob.add_plant(PrizeFlower("Prize", "Tulip", 40, "pink", 3))

    scores = GardenManager.create_garden_network()
    for g in GardenManager._gardens:
        if (g.validate_heights(g)):
            valid = True
        else:
            valid = False
    print(f"\nHeight validation test: {valid}")
    if (valid == True):
        print(f"Garden scores - Alice: {scores['Alice']}, "
              f"Bob: {scores['Bob']}")
        print(f"Total gardens managed: {GardenManager.total_gardens()}")
