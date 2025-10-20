from enum import Enum

from Commands.BaseCommand import Command
from Data_structures.SingletonPattern import Singleton
from Data_structures.StateMachine import StateMachine
from Commands.BUY import BuyResponses as br


class BuyCommand(metaclass=Singleton, Command):
    class BuyStates(Enum):
        INIT = 0
        INVALID_STOCK = 3
        VALID_STOCK_WHOLE = 1
        VALID_STOCK_FRACTIONAL = 2
        INVALID_QTT = 5
        VALID_QTT = 4
        OVER_BUDGET = 6
        REJECTED = 8
        CONFIRMED = 7

    def __init__(self):
        transitions = self.parse_user_input
        response_map = {
            BuyCommand.BuyStates.INIT: br.INTRO,
            BuyCommand.BuyStates.INVALID_STOCK: br.INVALID_STOCK,
            BuyCommand.BuyStates.VALID_STOCK_WHOLE: br.VALID_STOCK_WHOLE,
            BuyCommand.BuyStates.VALID_STOCK_FRACTIONAL: br.VALID_STOCK_FRACTIONAL,
            BuyCommand.BuyStates.INVALID_QTT: br.INVALID_QTT,
            BuyCommand.BuyStates.VALID_QTT: br.VALID_QTT,
            BuyCommand.BuyStates.OVER_BUDGET: br.OVER_BUDGET,
            BuyCommand.BuyStates.REJECTED: br.REJECTED,
            BuyCommand.BuyStates.CONFIRMED: br.CONFIRMED,
        }
        init_state = BuyCommand.BuyStates.INIT
        final_states = {
            BuyCommand.BuyStates.INVALID_STOCK,
            BuyCommand.BuyStates.INVALID_QTT,
            BuyCommand.BuyStates.OVER_BUDGET,
            BuyCommand.BuyStates.REJECTED,
            BuyCommand.BuyStates.CONFIRMED,
        }
        fsm = StateMachine(transitions, response_map, init_state, final_states)
        super().__init__(fsm)

    def parse_user_input(self, user_input):
        # match self.state_machine.current_state:
        #     case BuyCommand.BuyStates.INIT:
        #     case BuyCommand.BuyStates.VALID_STOCK_WHOLE:
        #     case BuyCommand.BuyStates.VALID_STOCK_FRACTIONAL:
        #     case BuyCommand.BuyStates.INVALID_STOCK:
        #     case BuyCommand.BuyStates.VALID_QTT:
        #     case BuyCommand.BuyStates.INVALID_QTT:
        #     case BuyCommand.BuyStates.OVER_BUDGET:
        #     case BuyCommand.BuyStates.REJECTED:
        #     case BuyCommand.BuyStates.CONFIRMED:
        pass

