#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    leght = len(my_list)

    new_list = []

    new_list = my_list

    if idx < 0 or idx >= leght:
        return my_list

    for i in range(leght):
        if i == idx:
            new_list[i] = element
        else:
            new_list[i] = new_list[i]

    return new_list
