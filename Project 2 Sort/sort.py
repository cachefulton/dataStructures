'''
Project Name: Project 2 Sort
Author: Cache Fulton
Due Date: 9/25/21
Course: CS2420-001

In this project we learn how to use Quicksort, Mergesort,
Insertion Sort, Selection Sort, and Timsort (builtin to Python).
'''
import random as r
import time as t

def quicksort(lyst):
    # [54, 26, 93, 17, 77, 31, 44, 55, 20]

    if len(lyst) <= 1:
        # no need to sort
        return lyst

    # select pivot
    # pivot = 20
    pivot = lyst[-1]

    # start left check keep checking until you find greater than pivot
    # [54, 26, 93, 17, 77, 31, 44, 55, 20]

    right_check = len(lyst) - 2 #-2 because our pivot is the last number

    is_split_found = False
    left_check_idx = -1

    while not is_split_found and left_check_idx <= len(lyst):
        left_check_idx += 1

    # for left_check_idx in range(len(lyst)):
        # If I'm looking at a number that is less than the pivot, leave it alone
        if lyst[left_check_idx] < pivot:
            pass

        elif lyst[left_check_idx] == pivot:
            # pivot in right place, but still sort left items
            sorted_left_side_list = quicksort(lyst[:-1])
            is_split_found = True


            lyst = sorted_left_side_list + [lyst[-1]]

        else:
            # we've found left item greater than pivot
            # find 54 (because it greater than 20)

            # start right check and look until you find value less than pivot
           
            while lyst[right_check] > pivot and right_check >= 0:
                right_check -= 1


            # find 17

            # if the right check is still greater than the left, swap those positions
            if right_check > left_check_idx:
                #swap 54 and 17
                lyst[left_check_idx], lyst[right_check] = lyst[right_check], lyst[left_check_idx]
                # [17, 26, 93, 54, 77, 31, 44, 55, 20]

                # continue checking

            else:
                # else swap right check with pivot
                pvt_idx = len(lyst) - 1
                lyst[pvt_idx], lyst[left_check_idx] = lyst[left_check_idx], lyst[pvt_idx]
                # first pass - [17, 20, 93, 54, 77, 31, 44, 55, 26]
                new_pvt_idx = left_check_idx

                # reset the pivot for the loop to refer to 
                # pivot = lyst[-1]


                # make list on left and right of pivot
                left_items_list = lyst[:new_pvt_idx]
                # [17]
                right_items_list = lyst[new_pvt_idx+1:]
                # [ 93, 54, 77, 31, 44, 55, 26]

                sorted_left_side_list = quicksort(left_items_list)
                sorted_right_side_list = quicksort(right_items_list)

                is_split_found = True

                full_list_again = sorted_left_side_list + [lyst[new_pvt_idx]] + sorted_right_side_list

                lyst = full_list_again
                # second pass - [17, 20, 93, 54, 77, 31, 44, 55, 26]
            
    return lyst
        
def mergesort(lyst):
    if len(lyst) > 1:
        mid = len(lyst) // 2
        left_lyst = lyst[:mid]
        right_lyst = lyst[mid:]
        sorted_right = mergesort(left_lyst)
        sorted_left = mergesort(right_lyst)
        #iterate and compare my lists
        left_look_at = 0
        right_look_at = 0
        output =[]
        while left_look_at < len(sorted_left) and right_look_at < len(sorted_right):
            if sorted_left[left_look_at] < sorted_right[right_look_at]:
                output.append(sorted_left[left_look_at])
                left_look_at += 1
            else:
                output.append(sorted_right[right_look_at])
                right_look_at += 1
        output.extend(sorted_left[left_look_at:])
        output.extend(sorted_right[right_look_at:])
        return output
    else:
        return lyst
        
    
def selection_sort(lyst):
    last_place = len(lyst) - 1
    while last_place >= 0:
        look_at = 0
        remember = 0
        while look_at < last_place:
            look_at += 1
            if lyst[remember] < lyst[look_at]:
                remember = look_at
        lyst[remember], lyst[last_place] = lyst[last_place], lyst[remember]
        last_place -= 1
    return lyst
        
def insertion_sort(lyst):
    remember_pos = -1
    for i in lyst:
        remember_pos += 1
        position = remember_pos
        while i < lyst[position - 1] and position > 0:
            lyst[position] = lyst[position - 1]
            position -= 1
        lyst[position] = i
    return lyst
            
def is_sorted(lyst):
    index = 0
    while index + 1 <= len(lyst) - 1:
        if isinstance(lyst[index], int) or isinstance(lyst[index + 1, int]) == False:
            return False
        if lyst[index] > lyst[index + 1]:
            return False
        else:
            index += 1
    return True

def timsort(lyst):
    return lyst.sort()

def time_function(function, lyst):
    start = t.perf_counter()
    hi = function(lyst)
    print(hi)
    stop = t.perf_counter()
    return stop - start

def main():
    lyst = r.sample(range(50000), k=15000)
    quick_list = lyst.copy()
    merge_list = lyst.copy()
    sel_list = lyst.copy()
    insert_list = lyst.copy()
    lystB = [17, 26, 93, 54, 77, 31, 44, 55, 20]
    # lystB = [10, 30, 20, 5]
    # quick = time_function(quicksort, quick_list)
    merge = time_function(mergesort, lystB)
    # selection = time_function(selection_sort, sel_list)
    # insertion = time_function(insertion_sort, insert_list)
    # tim = time_function(timsort, lyst) 

    # print("Quicksort time:", quick)
    print("Mergesort time:", merge)
    # print("Selection sort time:", selection)
    # print("Insertion sort time:", insertion)
    # print("Timsort time:", tim)

if __name__ == "__main__":
    main()