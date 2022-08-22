from .interfaces import Iabilities


class Archer(Iabilities):

    def __init__(self, level):
        self.level = level

    def ability(self):
        """What the archer do"""
        print("Throw arrows")

    def attribute_level(self):
        """Archer's level"""
        print(f"Level: {self.level}")
