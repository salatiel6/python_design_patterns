from .interface import ValidatorInterface


class MeatValidator(ValidatorInterface):
    def __init__(self, food: str):
        self.food = food

    def validate(self) -> bool:
        if self.food == "meat":
            return True

        return False

    def action(self) -> None:
        print(self.food)
