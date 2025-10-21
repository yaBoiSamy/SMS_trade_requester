from enum import Enum

from Commands.BaseCommand import Command
from Data_structures.SingletonPattern import Singleton
from Data_structures.StateMachine import StateMachine
from Questrade_Interface.Transaction import Transaction
from Data_structures.Logger import Logger
from Commands.BUY import BuyResponses as br
from Questrade_Interface.APIManager import QuestradeAPIManager


class BuyCommand(Command, metaclass=Singleton):
    class BuyStates(Enum):
        INIT = 0
        INVALID_SYMBOL = 1
        VALID_SYMBOL = 2
        INVALID_QTT = 4
        VALID_QTT = 5
        OVER_BUDGET = 6
        REJECTED = 8
        CONFIRMED = 7

    def __init__(self):
        transitions = self.parse_user_input
        response_map = self.perform_response
        init_state = BuyCommand.BuyStates.INIT
        final_states = {
            BuyCommand.BuyStates.INVALID_SYMBOL,
            BuyCommand.BuyStates.INVALID_QTT,
            BuyCommand.BuyStates.OVER_BUDGET,
            BuyCommand.BuyStates.REJECTED,
            BuyCommand.BuyStates.CONFIRMED,
        }
        fsm = StateMachine(transitions, response_map, init_state, final_states)
        super().__init__(fsm, True, self.on_termination())
        self.current_transaction = None

    def parse_user_input(self, user_input):
        user_input = user_input.lower().strip()
        match self.state_machine.current_state:
            case BuyCommand.BuyStates.INIT:
                self.current_transaction.code = user_input.capitalize()
                try:
                    self.current_transaction.unit_price = QuestradeAPIManager().get_share_value(self.current_transaction.code)
                    return BuyCommand.BuyStates.VALID_SYMBOL
                except ValueError:
                    return BuyCommand.BuyStates.INVALID_SYMBOL
            case BuyCommand.BuyStates.VALID_SYMBOL:
                self.current_transaction.qtt = int(user_input)
                return BuyCommand.BuyStates.VALID_QTT
            case BuyCommand.BuyStates.VALID_QTT:
                if user_input == "y" or user_input == "yes":
                    # PERFORM TRANSACTION
                    self.current_transaction.capture_time()
                    Logger().append_row(*self.current_transaction.to_tuple())
                    return BuyCommand.BuyStates.CONFIRMED
                elif user_input == "n" or user_input == "no":
                    return BuyCommand.BuyStates.REJECTED
                print("Answer unclear")
                return BuyCommand.BuyStates.VALID_QTT

    def perform_response(self):
        match self.state_machine.current_state:
            case BuyCommand.BuyStates.INIT:
                self.current_transaction = Transaction("Buy")
                return br.INTRO
            case BuyCommand.BuyStates.VALID_SYMBOL: return br.VALID_STOCK
            case BuyCommand.BuyStates.INVALID_SYMBOL: return br.INVALID_STOCK
            case BuyCommand.BuyStates.VALID_QTT: return br.VALID_QTT(self.current_transaction.get_total())
            case BuyCommand.BuyStates.INVALID_QTT: return br.INVALID_QTT
            case BuyCommand.BuyStates.OVER_BUDGET: return br.OVER_BUDGET
            case BuyCommand.BuyStates.REJECTED: return br.REJECTED
            case BuyCommand.BuyStates.CONFIRMED: return br.CONFIRMED

    def on_termination(self):
        self.current_transaction = None
