from src import Character, Archer, Priest, Warrior

archer = Character(Archer(6))
archer.action()
archer.level()

priest = Character(Priest(7))
priest.action()
priest.level()

warrior = Character(Warrior(5))
warrior.action()
warrior.level()
