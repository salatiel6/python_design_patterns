from .interfaces import Observer


class Person(Observer):
    def __init__(self):
        self.awake = False

    def is_awaken(self):
        return self.awake

    def update(self):
        print("Woke Up")
        self.awake = True