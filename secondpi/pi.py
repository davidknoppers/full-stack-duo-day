#!/usr/bin/python3
"""
Queries the Wolfram Alpha API to get the digits of pi
Dependencies: sudo pip3 install wolframalpha
Only works for about 1600 digits because the API hangs up on anything bigger
"""
import sys

def pi(n):
    if not n:
        return
    if type(n) is not int or type(n) is bool:
        return
    import wolframalpha
    client = wolframalpha.Client("2LPEY5-EK7VJA2EGH")
    digit_query = "first {} digits of pi".format(n)
    res = client.query(digit_query)
    i = 0
    for pod in res.pods:
        i += 1
        if i == 2:
            result = (pod['subpod']['plaintext'])
    return ("The first {} digits of pi:\n{}".format(n, result.split('.')[1]))
try:
    number = int(sys.argv[1])
    print(pi(number))
except:
    print("Usage: ./pi.py [integer]")
    print("Only works for about 1600 digits or less")
