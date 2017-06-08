#!/usr/bin/python3
"""
Brute-force computes the distance between all points in an array
Then returns the shortest distance
Requires 2D array of ints or an array of tuples of ints
"""
def distance(pair1, pair2, dimensions=2):
    if dimensions == 2:
        return (pair1[0] - pair2[0])**2 + (pair1[1] - pair2[1])**2
    else:
        return (pair1[0] - pair2[0])**2 + (pair1[1] - pair2[1])**2 + (pair1[2] - pair2[2])**2

def brute_force_closest_pair(array=None):
    if not array:
        return ("input needs an array")
    if not isinstance(array, list):
        return("input needs to be an array")
    if len(array) < 2:
        return("needs at least two elements")
    checklength = len(array[0])
    for i in array:
        if len(i) != checklength:
            return ("Length of each subarray must be consistent")
    if checklength != 2 and checklength != 3:
        return ("Subarrays must be of length 2 or 3")
    best = None
    first_pair = None
    second_pair = None
    for i in range(len(array) - 1):
        for j in range(i, len(array) - 1):
            if array[i] != array[j]:
                temp = distance(array[i], array[j], checklength)
                if best is None or temp < best:
                    first_pair = array[i]
                    second_pair = array[j]
                    best = temp
    return "closest pairs: {} and {}".format(first_pair, second_pair)

testarr = [(1,1), (2, 3), (1, 0), (3, 7), (4, 8), (6, 10), (-1, 3), (-2, 5), (3, -8)]
testarr3d = [(1, 2, 3), (0, 1, 3), (4, 6, 3), (6, 3, 2)]
print(brute_force_closest_pair(testarr3d))
