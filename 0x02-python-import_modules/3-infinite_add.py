#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    index = len(argv)
    s = 0
    if index == 1:
        print(s)
    else:
        for i in range(1, index):
            s += int(argv[i])
        print(s)
