#!/usr/bin/python3
def best_score(a_dictionary):
    best_key = None
    if a_dictionary:
        for key in a_dictionary:
            if best_key:
                if a_dictionary[best_key] < a_dictionary[key]:
                    best_key = key
                continue;
            best_key = key
    return best_key
