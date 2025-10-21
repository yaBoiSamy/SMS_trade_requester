

class Valuation:
    def __init__(self, currency, price):
        self.currency = currency
        self.price = price
        self.CAN_TO_USD = 0.71
        self.USD_TO_CAN = 1 / self.CAN_TO_USD

    def to_usd(self):
        if self.currency == 'USD':
            return self.price
        return self.price * self.CAN_TO_USD

    def to_can(self):
        if self.currency == 'CAN':
            return self.price
        return self.price * self.CAN_TO_USD

    def __gt__(self, other):
        return self.to_usd() > other.to_usd()

    def __lt__(self, other):
        return self.to_usd() < other.to_usd()

    def __eq__(self, other):
        return self.to_usd() == other.to_usd()

    def __ge__(self, other):
        return self.to_usd() >= other.to_usd()

    def __le__(self, other):
        return self.to_usd() <= other.to_usd()

    def update_fx(self):
        # TODO: Questrade call to exchange rates
        pass

