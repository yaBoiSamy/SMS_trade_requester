INTRO = """\
Enter the stock code
ex: NVDA for nvidia
"""

INVALID_STOCK = """\
This stock does not exist\
"""

VALID_STOCK_WHOLE = """\
Enter share quantity (whole)
"""

VALID_STOCK_FRACTIONAL = """\
Enter share quantity (fractional)
"""

INVALID_QTT = """\
This share quantity is invalid\
"""

VALID_QTT = lambda price: f"""\
Transaction receipt:
Total price: {price}$
Confirm transaction? (y/n)
"""

OVER_BUDGET = """\
This purchase is over-budget\
"""

REJECTED = """\
Purchase rejected\
"""

CONFIRMED = """\
Purchase confirmed
This transaction is now pending\
"""
