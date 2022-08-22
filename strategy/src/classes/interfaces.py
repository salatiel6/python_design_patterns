from abc import ABC, abstractmethod


class Iabilities(ABC):
    """Interface containing the relevant attribuites a character must have"""

    @abstractmethod
    def ability(self):
        """What the character does"""
        pass

    @abstractmethod
    def attribute_level(self):
        """Character's level"""
        pass
