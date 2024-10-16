# quicksort.py
import random

ARRAY_MAX = 100

def swap_integers(numbers, i, j):
    numbers[i], numbers[j] = numbers[j], numbers[i]

def partition_array(numbers, start, end, pivot_index):
    pivot_value = numbers[pivot_index]
    swap_integers(numbers, pivot_index, end)
    store_index = start
    for i in range(start, end):
        if numbers[i] < pivot_value:
            swap_integers(numbers, i, store_index)
            store_index += 1
    swap_integers(numbers, store_index, end)
    return store_index

def find_kth_smallest(numbers, start, end, k):
    if start == end:
        return numbers[start]
    pivot_index = random.randint(start, end)
    pivot_index = partition_array(numbers, start, end, pivot_index)
    if k == pivot_index:
        return numbers[k]
    elif k < pivot_index:
        return find_kth_smallest(numbers, start, pivot_index - 1, k)
    else:
        return find_kth_smallest(numbers, pivot_index + 1, end, k)

if __name__ == "__main__":
    numbers = [3, 2, 1, 5, 6, 4]
    array_size = len(numbers)
    k = 3

    print("Array:", numbers)
    result = find_kth_smallest(numbers, 0, array_size - 1, k - 1)
    print(f"The {k}th smallest element is: {result}")

##output
Array: [3, 2, 1, 5, 6, 4]
The 3th smallest element is: 3
