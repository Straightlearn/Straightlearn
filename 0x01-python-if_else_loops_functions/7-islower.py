#!/usr/bin/python3
def islower(c):
    """Checks for lowercase character."""
    charAscii = ord(c)
    if charAscii in range(97, 123):
        return True
    return False
