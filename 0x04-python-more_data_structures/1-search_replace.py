#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = []
    for i in my_list:
        if i == 2:
            new_list.append(89)
            continue;
        new_list.append(i)
    return new_list
