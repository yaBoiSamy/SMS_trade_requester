BUY_INTRO = """\
Enter the stock code
ex: NVDA for nvidia\
"""

BUY_VALID_STOCK_WHOLE = """\
Enter share quantity (whole)\
"""

BUY_VALID_STOCK_FRACTIONAL = """\
Enter share quantity (fractional)\
"""

INVALID_STOCK = """\
This stock does not exist\
"""

VALID_QTT = f"""\
Transaction receipt:
Price: {price}\
Sam's commission: 0.50$
Total cost: {price + 0.5}
Confirm transaction? (y/n)
"""

INVALID_QTT = """\
This share quantity is invalid\
"""

OVER_BUDGET = """\
This purchase is over-budget\
"""

CONFIRMED = """\
Purchase confirmed
This transaction is now pending\
"""

REJECTED = """\
Purchase rejected\
"""
