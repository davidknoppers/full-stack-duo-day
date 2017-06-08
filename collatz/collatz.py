#!/usr/bin/python3
import sys


def collatz(num):
    if not num:
        return ("nothing passed to function")
    count = 0
    while num != 1:
        if num % 2 == 0:
            num = num // 2
            count += 1
        else:
            num = (3*num) + 1
            count += 1
    return count


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 collatz.py number")
    else:
        try:
            count = int(sys.argv[1])
        except TypeError:
            print("input must be an integer")
        print(collatz(count))
