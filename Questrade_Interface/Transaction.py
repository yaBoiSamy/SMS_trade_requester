from datetime import datetime


class Transaction:
    def __init__(self, exchange_type=None, code=None, unit_price=None, qtt=None):
        self.time = datetime.now()
        self.exchange_type = exchange_type
        self.code = code
        self.unit_price = unit_price
        self.qtt = qtt

    def capture_time(self):
        self.time = datetime.now()

    def time_to_string(self):
        return f"{self.time.year}-{self.time.month:02}-{self.time.day:02} {self.time.hour:02}:{self.time.minute:02}:{self.time.second:02}"

    def get_total(self):
        return self.unit_price * self.qtt * (-1 if self.exchange_type == "Buy" else 1)

    def to_tuple(self):
        return self.time_to_string(), self.exchange_type, self.code, self.unit_price, self.qtt, self.get_total()
