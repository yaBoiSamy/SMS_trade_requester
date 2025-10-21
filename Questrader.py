from Commands.HELP.HelpCommand import HelpCommand
from Commands.BUY.BuyCommand import BuyCommand
from Commands.SELL.SellCommand import SellCommand
from Commands.LOGIN.LoginCommand import LoginCommand
from Commands.LOGOUT.LogoutCommand import LogoutCommand
from Commands.PENDING.PendingCommand import PendingCommand
from Commands.STATUS.StatusCommand import StatusCommand
from Commands.TAB.TabCommand import TabCommand

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
            "/buy": BuyCommand(),
            "/login": LoginCommand(),
            "/logout": LogoutCommand(),
            "/sell": SellCommand(),
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
                self.command_map[input(">>> ").lower().strip()].called()
            except KeyError as e:
                print("This is not a valid command.\nType /help for more information.")