from datetime import datetime
from Questrade_Interface.Valuation import Valuation


class Transaction:
    def __init__(self, exchange_type=None, symbol=None, valuation=None, qtt=None):
        self.time = datetime.now()
        self.exchange_type = exchange_type
        self.symbol = symbol
        self.valuation = valuation
        self.qtt = qtt

    def capture_time(self):
        self.time = datetime.now()

    def time_to_string(self):
        return f"{self.time.year}-{self.time.month:02}-{self.time.day:02} {self.time.hour:02}:{self.time.minute:02}:{self.time.second:02}"

    def get_total(self):
        return Valuation(self.valuation.currency, self.valuation.price * self.qtt * (-1 if self.exchange_type == "Buy" else 1))

    def to_tuple(self):
        return self.time_to_string(), self.exchange_type, self.symbol, self.valuation.currency, self.valuation.price, self.qtt, self.get_total()
