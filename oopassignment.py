# Assignment 1: Design Your Own Class! 🏗️
# Create a class representing anything you like (a Smartphone, Book, or even a Superhero!).
# Add attributes and methods to bring the class to life!
# Use constructors to initialize each object with unique values.
# Add an inheritance layer to explore polymorphism or encapsulation.

class Character:
    def __init__(self, name, power, universe):
        self.name = name
        self.power = power
        self.universe = universe

    def introduce(self):
        return f"I am {self.name} from the {self.universe} universe. My power is {self.power}."

    def use_power(self):
        return f"{self.name} uses {self.power}!"
class Superhero(Character):
    def __init__(self, name, power, universe, costume_color, catchphrase):
        super().__init__(name, power, universe)
        self.costume_color = costume_color
        self.catchphrase = catchphrase

    def say_catchphrase(self):
        return f"{self.name} says: '{self.catchphrase}'"

    def fly(self):
        return f"{self.name} takes to the skies in a flash of {self.costume_color}!"
class Villain(Character):
    def __init__(self, name, power, universe, evil_plan):
        super().__init__(name, power, universe)
        self.evil_plan = evil_plan

    def reveal_plan(self):
        return f"{self.name} reveals their evil plan: {self.evil_plan}"

    def laugh_evil(self):
        return f"{self.name} laughs maniacally: 'Mwahahaha!'"
hero = Superhero("SolarFlare", "Light Manipulation", "NeoVerse", "gold", "Here comes the light!")
villain = Villain("ShadowHex", "Dark Magic", "NeoVerse", "Plunge the world into darkness.")

print(hero.introduce())
print(hero.fly())
print(hero.say_catchphrase())

print(villain.introduce())
print(villain.reveal_plan())
print(villain.laugh_evil())

# ✅ Features Demonstrated:
# Classes & Objects

# Constructors (__init__)

# Inheritance

# Polymorphism (e.g., introduce() behaves differently for each subclass)

# Encapsulation (attributes and methods belong to each class appropriately)