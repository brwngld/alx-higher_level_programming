#!/usr/bin/python3

import sys

count = len(sys.argv) - 1

print("Number of argument(s):", end=" ")
if count == 0:
    print(".", end="\n\n")
elif count == 1:
    print("1 argument:")
    print("1:", sys.argv[1])
else:
    print(count, "arguments:")

    for i in range(1, count + 1):
        print(i, ":", sys.argv[i])
