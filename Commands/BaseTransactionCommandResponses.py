INTRO = """\
Enter the stock code
ex: NVDA for nvidia
"""

INVALID_SYMBOL = """\
This stock does not exist\
"""

VALID_SYMBOL = """\
Enter share quantity
"""

INVALID_QTT = """\
This share quantity is invalid\
"""

VALID_QTT = lambda valuation: f"""\
Transaction receipt:
Total price: {valuation.price}$ {valuation.currency}
Confirm transaction? (y/n)
"""

OVER_BUDGET = """\
This transaction is over-budget\
"""

REJECTED = """\
Transaction rejected\
"""

CONFIRMED = """\
Transaction confirmed
This transaction is now pending\
"""