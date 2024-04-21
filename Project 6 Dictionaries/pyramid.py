'''
Project Name: #6 Dictionaries
Author: Cache Fulton
Due Date: 11/20/21
Course: CS2420-001

Here we compute the weight each person holds from a pyramid of people
with each person weighing 200 pounds. We cache each new person.
'''
import sys
from hashmap import HashMap
from time import perf_counter

weight = 200
cache = HashMap()

number_cache_calls = 0
number_function_calls = 0

def weight_on(row, col):
    global number_cache_calls
    global number_function_calls
    number_function_calls += 1

    try:
        weight_ind = cache.get((row, col)) # if get() doesn't work, it will return keyerror
        number_cache_calls += 1
        return weight_ind
    except:
        # all if statements below are based on the structure of the pyramid
        if row == 0:
            result = 0.00
        elif col == 0:
            result = (weight + weight_on(row - 1, col)) / 2 
        elif row == col:
            result = (weight + weight_on(row - 1, col - 1)) / 2
        else:
            result = weight + (weight_on(row - 1, col - 1) + weight_on(row - 1, col)) / 2
    cache.set((row, col), result)
    return result

def main():
    try:
        rows = int(sys.argv[1])
    except:
        rows = 7
    f = open("part3.txt", 'w')
    start = perf_counter()

    for i in range(rows):
        for j in range(i + 1):
            f.write(f"{weight_on(i, j):.2f} ")
        f.write('\n')

    stop = perf_counter()
    f.write(f"\nElapsed time: {stop - start} seconds\n")
    f.write(f"Number of function calls: {number_function_calls}\n")
    f.write(f"Number of cache hits: {number_cache_calls}")
    
    f.close()

if __name__ == "__main__":
    main()
