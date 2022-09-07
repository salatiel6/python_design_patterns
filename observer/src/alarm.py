from .person import Person


class Alarm:
    def __init__(self):
        self.beep = False
        self.sleeping = []

    def add_person(self, person: Person):
        self.sleeping.append(person)

    def alarm_status(self):
        return self.beep

    def ring(self):
        self.beep = True

        for person in self.sleeping:
            person.update()

        self.sleeping = []
