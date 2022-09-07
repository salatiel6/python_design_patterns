from src import Alarm, Person

alarm = Alarm()
people = []
for _ in range(0, 3):
    people.append(Person())

for person in people:
    print(person.is_awaken())

for person in people:
    alarm.add_person(person)

alarm.ring()