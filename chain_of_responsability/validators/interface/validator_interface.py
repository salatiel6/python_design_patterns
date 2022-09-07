from abc import ABC, abstractmethod


class ValidatorInterface(ABC):
    @abstractmethod
    def validate(self) -> bool:
        pass

    @abstractmethod
    def action(self) -> None:
        pass
