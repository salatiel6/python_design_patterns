from commands import CommandInterface


class Button:
    def __init__(self) -> None:
        self.__command = None

    def set_command(self, command: CommandInterface) -> None:
        self.__command = command

    def action(self) -> None:
        if self.__command:
            self.__command.execute()