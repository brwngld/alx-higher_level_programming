#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    j = 0

    for k in range(x):
        try:
            print("{:d}".format(my_list[k]), end="")
            j += 1
        except (ValueError, TypeError):
            continue
    print()
    return j
