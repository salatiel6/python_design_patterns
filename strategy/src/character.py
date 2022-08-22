class Character:
    """Main concept of the character"""

    def __init__(self, character_class):
        self.character_class = character_class

    def action(self):
        """What the carachter does"""
        self.character_class.ability()

    def level(self):
        """Character's level"""
        self.character_class.attribute_level()
