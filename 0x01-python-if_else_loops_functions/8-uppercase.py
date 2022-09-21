#!/usr/bin/python3
def uppercase(str):
    """Converts all lowercase characters to uppercase."""
    uppercase = ""
    for i in str:
        if ord(i) in range(97, 123):
            uppercase += chr(ord(i) - 32)
        else:
            uppercase += i
    print("{:s}".format(uppercase))
        
