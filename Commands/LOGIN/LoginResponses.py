INTRO = """\
Enter password
"""

INVALID_PASSWORD = lambda attempts: f"""\
Incorrect password
{attempts} attempts remaining
"""

LOCKED_OUT = """\
Too many failed attempts.
Your account is locked out.
Go see Sam to unlock it"""

VALID_PASSWORD = """\
Login successful\
"""
