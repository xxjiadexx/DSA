import time
import random

# Bubble Sort
def bubbleSort(array):
    n = len(array)
    for i in range(n-1):
        swapped = False
        for j in range(n-1-i):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                swapped = True
        if not swapped:
            break

# Selection Sort
def selectionSort(array):
    n = len(array)
    for i in range(n-1):
        min_pos = i
        for j in range(i+1, n):
            if array[j] < array[min_pos]:
                min_pos = j
        array[i], array[min_pos] = array[min_pos], array[i]

# Insertion Sort
def insertionSort(array):
    n = len(array)
    for i in range(1, n):
        temp = array[i]
        j = i - 1
        while j >= 0 and temp < array[j]:
            array[j+1] = array[j]
            j -= 1
        array[j+1] = temp

# Merge Sort
def mergeSort(array):
    if len(array) <= 1:
        return array
    mid = len(array) // 2
    leftSorted = mergeSort(array[:mid])
    rightSorted = mergeSort(array[mid:])
    return merge(leftSorted, rightSorted)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Function to measure execution time
def measure_time(sort_function, array):
    start = time.time()
    if sort_function == mergeSort:
        sorted_array = sort_function(array)  # Merge Sort returns a new list
        array[:] = sorted_array  # Update the original array
    else:
        sort_function(array)  # In-place sorting
    end = time.time()
    return end - start

# Main function
if __name__ == '__main__':
    size = 10000  # Change this value to test different dataset sizes
    original_array = [random.randint(1, 1000) for _ in range(size)]

    # Test each sorting algorithm
    for sort_name, sort_function in [
        ("Bubble Sort", bubbleSort),
        ("Selection Sort", selectionSort),
        ("Insertion Sort", insertionSort),
        ("Merge Sort", mergeSort),
    ]:
        test_array = original_array[:]  # Copy to avoid modifying original data
        time_taken = measure_time(sort_function, test_array)
        print(f"{sort_name}: {time_taken:.6f} seconds")
