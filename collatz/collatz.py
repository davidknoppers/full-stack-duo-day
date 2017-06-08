#!/usr/bin/python3

def collatz(num):
    if not num:
        return ("nothing passed to function")
    if not isinstance(num, int):
        return ("input must be an integer")
    count = 0
    while num != 1:
        if num % 2 == 0:
            num /= 2
            count += 1
        else:
            num = (3*num) + 1
            count += 1
    return count
print(collatz(75128138247))
print(collatz(2361235441021745907775))
