#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    new_list = []

    if idx < 0 or idx >= len(my_list):
        return my_list

    for i in my_list:
        new_list.append(i)

    for i in range(len(new_list)):
        if i == idx:
            new_list[i] = element
        else:
            new_list[i] = new_list[i]

    return new_list
