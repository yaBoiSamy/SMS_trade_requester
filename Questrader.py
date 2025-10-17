from Commands.HelpCommand import HelpCommand
from Data_structures.SingletonPattern import Singleton
import BotResponses as br


class Questrader(metaclass=Singleton):
    def __init__(self):
        self.command_map = {
            "/help": HelpCommand(),
        }
        print(br.INTRO)
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