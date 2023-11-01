#!/usr/bin/python3
def islower(c):
    return 97 <= ord(c) <= 123

def uppercase(str):
    for i in str:
            print("{:c}".format(ord(i) if not islower(i) else ord(i)-32), end="")
    print("")
