from encodings import search_function
from enum import Enum
from abc import ABC, abstractmethod

from Commands.BaseCommand import Command
from Data_structures.StateMachine import StateMachine
from Data_structures.Logger import Logger
from Questrade_Interface.Transaction import Transaction
from Commands import BaseTransactionCommandResponses as br
from Questrade_Interface.APIManager import QuestradeAPIManager


class TransactionCommand(ABC, Command):
    class TransactionStates(Enum):
        INIT = 0
        INVALID_SYMBOL = 1
        VALID_SYMBOL = 2
        INVALID_QTT = 4
        OVER_BUDGET = 6
        VALID_QTT = 5
        REJECTED = 6
        CONFIRMED = 7

    def __init__(self, transaction_type):
        transitions = self.parse_user_input
        response_map = self.perform_response
        init_state = TransactionCommand.TransactionStates.INIT
        final_states = {
            TransactionCommand.TransactionStates.INVALID_SYMBOL,
            TransactionCommand.TransactionStates.INVALID_QTT,
            TransactionCommand.TransactionStates.OVER_BUDGET,
            TransactionCommand.TransactionStates.REJECTED,
            TransactionCommand.TransactionStates.CONFIRMED,
        }
        fsm = StateMachine(transitions, response_map, init_state, final_states)
        super().__init__(fsm, True, self.on_termination)
        self.current_transaction = None
        self.transaction_type = transaction_type

    def parse_user_input(self, user_input):
        user_input = user_input.lower().strip()
        match self.state_machine.current_state:
            case TransactionCommand.TransactionStates.INIT:
                return self.parse_symbol(user_input)
            case TransactionCommand.TransactionStates.VALID_SYMBOL:
                return self.parse_symbol_qtt(user_input)
            case TransactionCommand.TransactionStates.VALID_QTT:
                return self.parse_confirmation(user_input)

    def parse_symbol(self, symbol):
        self.current_transaction.code = symbol.capitalize()
        try:
            self.current_transaction.valuation = QuestradeAPIManager().get_share_value(self.current_transaction.code)
            return TransactionCommand.TransactionStates.VALID_SYMBOL
        except ValueError:
            return TransactionCommand.TransactionStates.INVALID_SYMBOL

    def parse_symbol_qtt(self, symbol_qtt):
        try:
            self.current_transaction.qtt = int(symbol_qtt)
            if self.current_transaction.qtt < 0:
                return TransactionCommand.TransactionStates.INVALID_QTT
            balances = QuestradeAPIManager().get_balances()
            relevant_balance = balances[self.current_transaction.valuation.currency]
            if self.current_transaction.get_total() > relevant_balance:
                return TransactionCommand.TransactionStates.OVER_BUDGET
            return TransactionCommand.TransactionStates.VALID_QTT
        except ValueError:
            return TransactionCommand.TransactionStates.INVALID_QTT

    def parse_confirmation(self, confirmation):
        if confirmation == "n" or confirmation == "no":
            return TransactionCommand.TransactionStates.REJECTED
        if confirmation != "y" and confirmation != "yes":
            print("Answer unclear")
            return TransactionCommand.TransactionStates.VALID_QTT
        if not self.perform_sale():
            return TransactionCommand.TransactionStates.REJECTED

        self.current_transaction.capture_time()
        Logger().append_row(*self.current_transaction.to_tuple())
        return TransactionCommand.TransactionStates.CONFIRMED

    @abstractmethod
    def perform_sale(self):
        # PERFORM TRANSACTION
        pass

    def perform_response(self):
        match self.state_machine.current_state:
            case TransactionCommand.TransactionStates.INIT:
                self.current_transaction = Transaction(self.transaction_type)
                return br.INTRO
            case TransactionCommand.TransactionStates.INVALID_SYMBOL: return br.INVALID_SYMBOL
            case TransactionCommand.TransactionStates.VALID_SYMBOL: return br.VALID_SYMBOL
            case TransactionCommand.TransactionStates.VALID_QTT: return br.VALID_QTT(self.current_transaction.get_total())
            case TransactionCommand.TransactionStates.INVALID_QTT: return br.INVALID_QTT
            case TransactionCommand.TransactionStates.OVER_BUDGET: return br.OVER_BUDGET
            case TransactionCommand.TransactionStates.REJECTED: return br.REJECTED
            case TransactionCommand.TransactionStates.CONFIRMED: return br.CONFIRMED

    def on_termination(self):
        self.current_transaction = None

