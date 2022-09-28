#!/usr/bin/python3
def roman_to_int(roman_string):
    integer = 0
    roman_int = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100,
                 'D': 500, 'M': 1000}
    prev_numeral = ''

    if not roman_string:
        return integer

    for numeral in roman_string:
        if numeral not in roman_int:
            return 0
        if (prev_numeral and roman_int[prev_numeral] < roman_int[numeral]):
            integer += roman_int[numeral] - roman_int[prev_numeral] * 2
        else:
            integer += roman_int[numeral]
        prev_numeral = numeral
    return integer
