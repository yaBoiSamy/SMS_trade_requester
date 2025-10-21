from enum import Enum

from Commands.BaseCommand import Command
from Data_structures.SingletonPattern import Singleton
from Data_structures.StateMachine import StateMachine
from Data_structures.Logger import Logger
from Questrade_Interface.Transaction import Transaction
from Commands.SELL import SellResponses as br


class SellCommand(Command, metaclass=Singleton):
    class SellStates(Enum):
        INIT = 0
        INVALID_STOCK = 1
        VALID_STOCK_WHOLE = 2
        VALID_STOCK_FRACTIONAL = 3
        INVALID_QTT = 4
        VALID_QTT = 5
        REJECTED = 6
        CONFIRMED = 7

    def __init__(self):
        transitions = self.parse_user_input
        response_map = self.perform_response
        init_state = SellCommand.SellStates.INIT
        final_states = {
            SellCommand.SellStates.INVALID_STOCK,
            SellCommand.SellStates.INVALID_QTT,
            SellCommand.SellStates.REJECTED,
            SellCommand.SellStates.CONFIRMED,
        }
        fsm = StateMachine(transitions, response_map, init_state, final_states)
        super().__init__(fsm, True, self.on_termination)
        self.current_transaction = None

    def parse_user_input(self, user_input):
        user_input = user_input.lower().strip()
        match self.state_machine.current_state:
            case SellCommand.SellStates.INIT:
                self.current_transaction.code = user_input.capitalize()
                self.current_transaction.unit_price = 50  # GET UNIT PRICE HERE
                return SellCommand.SellStates.VALID_STOCK_WHOLE
            case SellCommand.SellStates.VALID_STOCK_WHOLE:
                self.current_transaction.qtt = int(user_input)
                return SellCommand.SellStates.VALID_QTT
            case SellCommand.SellStates.VALID_STOCK_FRACTIONAL:
                self.current_transaction.qtt = float(user_input)
                return SellCommand.SellStates.VALID_QTT
            case SellCommand.SellStates.VALID_QTT:
                if user_input == "y" or user_input == "yes":
                    # PERFORM TRANSACTION
                    self.current_transaction.capture_time()
                    Logger().appendRow(*self.current_transaction.to_tuple())
                    return SellCommand.SellStates.CONFIRMED
                elif user_input == "n" or user_input == "no":
                    return SellCommand.SellStates.REJECTED
                print("Answer unclear")
                return SellCommand.SellStates.VALID_QTT

    def perform_response(self):
        match self.state_machine.current_state:
            case SellCommand.SellStates.INIT:
                self.current_transaction = Transaction("Sell")
                return br.INTRO
            case SellCommand.SellStates.INVALID_STOCK: return br.INVALID_STOCK
            case SellCommand.SellStates.VALID_STOCK_WHOLE: return br.VALID_STOCK_WHOLE
            case SellCommand.SellStates.VALID_STOCK_FRACTIONAL: return br.VALID_STOCK_FRACTIONAL
            case SellCommand.SellStates.VALID_QTT: return br.VALID_QTT(self.current_transaction.get_total())
            case SellCommand.SellStates.INVALID_QTT: return br.INVALID_QTT
            case SellCommand.SellStates.REJECTED: return br.REJECTED
            case SellCommand.SellStates.CONFIRMED: return br.CONFIRMED

    def on_termination(self):
        self.current_transaction = None

