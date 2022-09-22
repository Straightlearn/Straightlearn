#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    argv = sys.argv
    if len(argv) > 2:
        print("{:d} {:s}".format(len(argv) - 1, "argument"))
    else:
        print("{:d} {:s}".format(len(argv) - 1, "arguments"))

    for i in range(1, len(argv)):
        print("{:d}: {:s}".format(i, argv[i]))
