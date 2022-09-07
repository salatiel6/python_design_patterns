import config_path # noqa

from button import Button
from receptor import Receptor
from commands import ButtonCommand

button = Button()
receptor = Receptor()

button.set_command(ButtonCommand(receptor, {"message": "Hello"}))
button.action()