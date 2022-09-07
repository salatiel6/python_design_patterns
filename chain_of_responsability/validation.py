from validators import FruitValidator, MeatValidator


class Validation:
    def __init__(self, food) -> None:
        self.food = food
        self.validators = [
            FruitValidator(food),
            MeatValidator(food)
        ]

    def process(self):
        for validator in self.validators:
            if validator.validate():
                return validator.action()
