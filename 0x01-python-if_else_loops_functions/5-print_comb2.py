#!/usr/bin/python3
for num in range(100):
    formatted_num = f"{num:02d}"
    if num == 99:
        print("{}".format(formatted_num))
    else:
        print("{}".format(formatted_num), end=', ')
