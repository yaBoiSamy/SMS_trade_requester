from Commands.HELP.HelpCommand import HelpCommand
from Data_structures.SingletonPattern import Singleton

INTRO = """\
Hi! This is Questrader version 1.0. 
I'll be taking care of your stocks from now on.
Type /help for a quick introduction to the accepted commands.\
"""


class Questrader(metaclass=Singleton):
    def __init__(self):
        self.command_map = {
            "/help": HelpCommand(),
        }
        print(INTRO)
        self.chat()

    def get_active_command(self):
        for command in self.command_map.values():
            if command.isActive:
                return command
        return None

    def chat(self):
        while True:
            try:
                self.command_map[input(">>> ")].called()
            except KeyError as e:
                print("This is not a valid command.\nType /help for more information.")