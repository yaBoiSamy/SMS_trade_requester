from Commands.BaseTransactionCommand import TransactionCommand
from Data_structures.SingletonPattern import Singleton


class SellCommand(TransactionCommand, metaclass=Singleton):

