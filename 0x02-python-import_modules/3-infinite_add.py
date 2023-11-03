#!/usr/bin/python3
if __name__ == "__main__":

    import sys
    total = 0
    n = int(len(sys.argv))
    for i in range(n - 1):
        total += int(sys.argv[i + 1])
    print("{}".format(total))
