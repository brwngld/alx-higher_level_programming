#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    add = 0
    for s in range(1, len(sys.argv)):
        add += int(sys.argv[s])

    print("{:d}".format(add))
