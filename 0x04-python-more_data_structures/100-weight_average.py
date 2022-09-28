#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    reduced_list = [score * weight for score, weight in my_list]
    total_weight = 0
    total_integers = 0

    for i in range(len(reduced_list)):
        total_weight += my_list[i][1]
        total_integers += reduced_list[i]

    return total_integers / total_weight
