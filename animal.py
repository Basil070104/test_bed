import random

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.health = 100
        self.energy = 100

    def eat(self, food_amount):
        if self.energy + food_amount <= 100:
            self.energy += food_amount
        else:
            self.energy = 100

    def sleep(self, hours):
        if self.health + hours <= 100:
            self.health += hours
        else:
            self.health = 100

    def play(self):
        if self.energy > 10:
            self.energy -= 10
            self.health -= 5
            print(f"{self.name} played and used some energy!")
        else:
            print(f"{self.name} is too tired to play.")

    def stats(self):
        print(f"Name: {self.name}, Species: {self.species}")
        print(f"Health: {self.health}, Energy: {self.energy}")


class Zoo:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def show_all_stats(self):
        for animal in self.animals:
            animal.stats()

    def random_event(self):
        random_animal = random.choice(self.animals)
        event_type = random.choice(["eat", "sleep", "play"])

        if event_type == "eat":
            food_amount = random.randint(5, 30)
            random_animal.eat(food_amount)
            print(f"{random_animal.name} ate {food_amount} units of food.")
        elif event_type == "sleep":
            hours = random.randint(1, 8)
            random_animal.sleep(hours)
            print(f"{random_animal.name} slept for {hours} hours.")
        elif event_type == "play":
            random_animal.play()

    def execute_day(self):
        print("Executing a new day in the zoo...")
        for _ in range(10):
            self.random_event()
        self.show_all_stats()

def main():
    zoo = Zoo()

    lion = Animal("Leo", "Lion")
    zebra = Animal("Zara", "Zebra")
    elephant = Animal("Ella", "Elephant")

    zoo.add_animal(lion)
    zoo.add_animal(zebra)
    zoo.add_animal(elephant)

    zoo.execute_day()

if __name__ == "__main__":
    main()
