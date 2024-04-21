"""
Project Name: Project 1 Search
Author: Cache Fulton
Due Date: 9/18/21
Course: CS2420-001

In this project we learn how to use binary, jump, and linear search.
"""

import random as r
import time as t
import math as m


def linear_search(lyst, target):
    for i in lyst:
        if i == target:
            return True
    return False


def binary_search(lyst, target):
    mid = (len(lyst) - 1) // 2
    low = 0
    high = len(lyst) - 1
    if (
        lyst[-1] == target or lyst[0] == target
    ):  # the while loop doesn't get the first or last values
        return True
    while mid > low:
        if lyst[mid] == target:
            return True
        elif lyst[mid] > target:
            high = mid
            mid = (low + high) // 2
        elif lyst[mid] < target:
            low = mid
            mid = (low + high) // 2
    return False


# this one works perfect, but, implemented poorly
# mid = (len(lyst)-1) // 2
# while mid >= 0:
#     if lyst[mid] == target:
#         return True
#     elif lyst[mid] > target:
#         low = 0 # reset low
#         high = mid
#         lyst = lyst[low:high]
#         mid = (len(lyst)-1) // 2
#     elif lyst[mid] < target:
#         high = len(lyst) - 1 #reset high
#         low = mid
#         lyst = lyst[low:high + 1]
#         mid = (len(lyst)-1) // 2
# return False

# don't know how to make it tail recursion
# div = (len(lyst)-1) // 2
# if div >= 0:
#     if lyst[div] == target:
#         return True
#     elif lyst[div] > target:
#         return binary_search(lyst[0:div], target)
#     elif lyst[div] < target:
#         return binary_search(lyst[div:], target)
# else:
#     return False


def jump_search(lyst, target):
    block = int(m.sqrt(len(lyst)))
    look_at = 0
    last_look = 0
    while lyst[look_at] < target:
        last_look = look_at
        look_at += block
        if look_at > len(lyst) - 1:
            look_at = len(lyst) - 1
            if lyst[-1] < target:
                return False
            break
    if lyst[look_at] >= target:
        for i in lyst[last_look : look_at + 1]:
            if i == target:
                return True
        return False


# don't know how to make it tail recursion
# step = 10000
# if lyst[0] == target:
#     return True
# elif lyst[step] < target:
#     return jump_search(lyst[step:], target)
# elif lyst[step] > target:
#     for i in lyst[0:step]:
#         if i == target:
#             return True
#     return False


def main():
    lyst = r.sample(range(10000000), k=9000000)
    lyst.sort()
    first = lyst[0]
    middle = lyst[(len(lyst) - 1) // 2 + 1]
    not_there = 1000000001

    start = t.perf_counter()
    linear_search(lyst, first)
    stop = t.perf_counter()
    print("First element linear", stop - start)
    start = t.perf_counter()
    linear_search(lyst, middle)
    stop = t.perf_counter()
    print("Middle element linear", stop - start)
    start = t.perf_counter()
    linear_search(lyst, not_there)
    stop = t.perf_counter()
    print("Not in the list linear", stop - start)

    start = t.perf_counter()
    binary_search(lyst, first)
    stop = t.perf_counter()
    print("First element binary", stop - start)
    start = t.perf_counter()
    binary_search(lyst, middle)
    stop = t.perf_counter()
    print("Middle element binary", stop - start)
    start = t.perf_counter()
    binary_search(lyst, not_there)
    stop = t.perf_counter()
    print("Not in the list binary", stop - start)

    start = t.perf_counter()
    jump_search(lyst, first)
    stop = t.perf_counter()
    print("First element jump", stop - start)
    start = t.perf_counter()
    jump_search(lyst, middle)
    stop = t.perf_counter()
    print("Middle element jump", stop - start)
    start = t.perf_counter()
    jump_search(lyst, not_there)
    stop = t.perf_counter()
    print("Not in the list jump", stop - start)


if __name__ == "__main__":
    main()
