#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):

    count = 0

    try:
        for i in range(x):
            if isinstance(my_list[i], int):
                print("{:d}".format(my_list[i]))
                count += 1
            else:
                continue
    except ValueError and IndexError:
        pass

    return count