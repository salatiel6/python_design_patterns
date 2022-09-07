from .insert import Insert
from .select import Select
from .delete import Delete


class Facade:
    def __init__(self):
        self.insert = Insert()
        self.select = Select()
        self.delete = Delete()

    def select_single_element(self):
        return self.select.select_single_element()

    def select_multiple_elements(self):
        return self.select.select_multiple_elements()

    def insert_single_element(self):
        return self.insert.insert_single_element()

    def insert_multiple_elements(self):
        return self.insert.insert_multiple_elements()

    def delete_single_elemet(self):
        return self.delete.delete_single_element()
