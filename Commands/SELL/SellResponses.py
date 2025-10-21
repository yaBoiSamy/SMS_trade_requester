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

VALID_QTT = lambda price: f"""\
Transaction receipt:
Total selling price: {price}$
Confirm transaction? (y/n)
"""

INVALID_QTT = """\
This share quantity is invalid\
"""

REJECTED = """\
Sale rejected\
"""

CONFIRMED = """\
Sale confirmed
This transaction is now pending\
"""
