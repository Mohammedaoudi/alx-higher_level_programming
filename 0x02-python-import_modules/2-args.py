#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    index = len(sys.argv) - 1
    if index == 0:
        print("{} arguments.".format(index))
    elif index == 1:
        print("{} argument:".format(index))
        print("{}: {}".format(index, sys.argv[index]))
    else:
        print("{} arguments:".format(index))
        for i in range(1, index + 1):
            print("{}: {}".format(i, sys.argv[i]))
