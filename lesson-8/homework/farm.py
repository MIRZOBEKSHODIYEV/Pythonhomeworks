class Animal:
    def __init__(self, name, age, species):
        self.name = name
        self.age = age
        self.species = species

    def eat(self):
        print(f"{self.name} the {self.species} is eating.")

    def sleep(self):
        print(f"{self.name} the {self.species} is sleeping.")

    def make_sound(self):
        print(f"{self.name} makes a generic animal sound.")

class Cow(Animal):
    def __init__(self, name, age):
        super().__init__(name, age, "Cow")

    def make_sound(self):
        print(f"{self.name} says 'Moo!'")

    def produce_milk(self):
        print(f"{self.name} is producing milk.")

class Chicken(Animal):
    def __init__(self, name, age):
        super().__init__(name, age, "Chicken")

    def make_sound(self):
        print(f"{self.name} says 'Cluck!'")

    def lay_egg(self):
        print(f"{self.name} laid an egg!")

class Goat(Animal):
    def __init__(self, name, age):
        super().__init__(name, age, "Goat")

    def make_sound(self):
        print(f"{self.name} says 'Billy!'")

    def roll_in_mud(self):
        print(f"{self.name} is rolling in the wool.")

# Example usage
def main():
    cow = Cow("Bessie", 5)
    chicken = Chicken("Henrietta", 2)
    goat = Goat("Porky", 3)

    farm_animals = [cow, chicken, goat]

    for animal in farm_animals:
        animal.eat()
        animal.sleep()
        animal.make_sound()

    # Specific behaviors
    cow.produce_milk()
    chicken.lay_egg()
    goat.roll_in_wool()

if __name__ == "__main__":
    main()