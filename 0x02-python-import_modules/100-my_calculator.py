#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    from calculator_1 import add, sub, mul, div

    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    a = int(argv[1])
    b = int(argv[3])
    operator = argv[2]

    if operator != "+" and operator != "-" and operator != "\
            *" and operator != "/":
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    if operator == "+":
        print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
    if operator == "-":
        print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))
    if operator == "*":
        print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))
    if operator == "/":
        print("{:d} / {:d} = {:d}".format(a, b, div(a, b)))
