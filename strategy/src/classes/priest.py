from .interfaces import Iabilities


class Priest(Iabilities):

    def __init__(self, level):
        self.level = level

    def ability(self):
        """What the priest do"""
        print("Heal partners")

    def attribute_level(self):
        """Priest's level"""
        print(f"Level: {self.level}")
