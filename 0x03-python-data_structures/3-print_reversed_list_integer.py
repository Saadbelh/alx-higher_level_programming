#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    i = 1
    for i in my_list:
        num = int(my_list[-i])
        print("{:d}".format(num))
