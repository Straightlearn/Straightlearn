#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    nb_print = 0

    for i in range(x):
        try:
            my_list[i]
        except IndexError:
            break
        nb_print += 1
    return nb_print
