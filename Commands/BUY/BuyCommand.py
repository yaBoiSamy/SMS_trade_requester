from enum import Enum

from Data_structures.SingletonPattern import Singleton
from Data_structures.StateMachine import StateMachine
from Commands.HELP import HelpResponses as br


class BuyCommand(metaclass=Singleton):
    class BuyStates(Enum):
        INIT = 0
        VALID_STOCK_WHOLE = 1
        VALID_STOCK_FRACTIONAL = 2
        INVALID_STOCK = 3
        VALID_QTT = 4
        INVALID_QTT = 5
        OVER_BUDGET = 6
        CONFIRMED = 7
        REJECTED = 8

    def __init__(self):
        transitions = {}
        response_map = {
            BuyCommand.BuyStates.INIT: br.HELP_INTRO
        }
        init_state = BuyCommand.BuyStates.INIT
        final_states = {
            BuyCommand.BuyStates.INVALID_STOCK,
            BuyCommand.BuyStates.INVALID_QTT,
            BuyCommand.BuyStates.OVER_BUDGET,
            BuyCommand.BuyStates.CONFIRMED,
            BuyCommand.BuyStates.REJECTED,
        }
        fsm = StateMachine(transitions, response_map, init_state, final_states)
        super().__init__(fsm)
