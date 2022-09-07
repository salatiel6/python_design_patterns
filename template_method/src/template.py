from random import randint
from abc import ABC, abstractmethod


class Template(ABC):
    def __init__(self, data: []):
        self.data = self.__format_data(data)

    @staticmethod
    def __format_data(data: []) -> {}:
        formatted_data = {
            "id": randint(0, 100),
            "nome": data[0],
            "idade": data[1]
        }

        return formatted_data

    @abstractmethod
    def insert_data_in_doc(self):
        pass
