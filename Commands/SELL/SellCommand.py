from Commands.Base.BaseTransactionCommand import TransactionCommand
from Questrade_Interface.APIManager import QuestradeAPIManager


class SellCommand(TransactionCommand):
    def __init__(self):
        super().__init__("Sell")

    def perform_transaction(self):
        return True
