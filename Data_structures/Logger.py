import pandas as pd
import os

from Data_structures.SingletonPattern import Singleton


class Logger(metaclass=Singleton):
    FILENAME = "Logs.csv"

    def __init__(self):
        if not os.path.exists(Logger.FILENAME):
            pd.DataFrame(columns=["Time", "Type", "Stock code", "Unit price", "Quantity", "Total"]).to_csv(Logger.FILENAME, index=False)
        self.df = pd.read_csv(Logger.FILENAME)

    def appendRow(self, time, transaction_type, stock_code, unit_price, qtt, total):
        self.df.loc[len(self.df)] = [time, transaction_type, stock_code, unit_price, qtt, total]
        self.df.to_csv(Logger.FILENAME, index=False)

    def get_logs(self):
        return self.df.to_string(index=False)
