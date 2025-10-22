from Commands.Base.BaseTransactionCommand import TransactionCommand
from Questrade_Interface.APIManager import QuestradeAPIManager


class BuyCommand(TransactionCommand):
    def __init__(self):
        super().__init__("Buy")

    def perform_transaction(self):
        return True
