from .interface import ValidatorInterface


class FruitValidator(ValidatorInterface):
    def __init__(self, food: str):
        self.food = food

    def validate(self) -> bool:
        if self.food == "fruit":
            return True

        return False

    def action(self) -> None:
        print(self.food)
