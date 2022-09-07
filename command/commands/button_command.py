from .interface import CommandInterface


class ButtonCommand(CommandInterface):
    def __init__(self, receptor, information) -> None:
        self.__receptor = receptor
        self.__message = self.__format_information(information)

    @staticmethod
    def __format_information(information):
        return information

    def execute(self) -> None:
        self.__receptor.process_information(self.__message)
