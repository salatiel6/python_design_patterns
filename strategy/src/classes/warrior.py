from .interfaces import Iabilities


class Warrior(Iabilities):

    def __init__(self, level):
        self.level = level

    def ability(self):
        """What the warrior do"""
        print("Fight with body or weapons")

    def attribute_level(self):
        """Warrior's level"""
        print(f"Level: {self.level}")
