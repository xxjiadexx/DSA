import random

def swap(array,start,end):
    array[start], array[end] = array[end], array[start]

def partition(array,start,end):
    n = len(array)
    pivotIndex = start
    pivotValue = array[start]

    while start < end:
        while start < n and array[start] <= pivotValue:
            start += 1
        while array[end] > pivotValue:
            end -= 1
        if start < end:
            swap(array,start,end)

    swap(array,pivotIndex,end)
    return end

def quickSort(array,start,end):
    if start < end:
        pi = partition(array,start,end)
        quickSort(array,start,pi-1)
        quickSort(array,pi+1,end)

def quickSelect(array,start,end,k):
    if start <= end:
        pi = partition(array,start,end)
        if pi == k:
            return array[pi]
        elif pi > k:
            return quickSelect(array,start,pi - 1, k)
        else:
            return quickSelect(array,pi + 1,end, k)


if __name__ == '__main__':
    import random

    arr1 = [34, 7, 23, 32, 5, 62, 32, 78, 12, 9, 54, 21, 45, 37, 8]
    arr2 = [93, 27, 65, 18, 50, 33, 99, 10, 73, 22, 87, 41, 3, 69, 90, 44, 57, 80, 29, 14]
    arr3 = [random.randint(0, 9999) for _ in range(10000)]

    ### Quick Sort (Needs Copy of Original List)
    quick1 = arr1[:]
    quick2 = arr2[:]
    quick3 = arr3[:]

    quickSort(quick1, 0, len(quick1) - 1)
    quickSort(quick2, 0, len(quick2) - 1)
    quickSort(quick3, 0, len(quick3) - 1)

    print(f'Quick Sort 1: {quick1}')
    print(f'Quick Sort 2: {quick2}')
    print(f'Quick Sort 3: {quick3[:10]} ... (truncated)\n')

    # Finding the k-th smallest element
    k = 5  # Change this to any k-th smallest element you want to find
    n = len(arr1)
    k_largest = n - k + 1

    print(f'The {k}-th smallest element in arr1 is {quickSelect(arr1[:], 0, len(arr1) - 1, k)}')
    print(f'The {k}-th smallest element in arr2 is {quickSelect(arr2[:], 0, len(arr2) - 1, k)}')
    print(f'The {k}-th smallest element in arr3 is {quickSelect(arr3[:], 0, len(arr3) - 1, k)}')
    print(
        f'The {k}-th largest element in arr1 is {quickSelect(arr1[:], 0, n - 1, k_largest)}')  # Fixed missing parenthesis

    # Finding multiple k-th largest elements
    arr5 = [34, 7, 23, 32, 5, 62, 32, 78, 12, 9, 54, 21, 45, 37, 8]
    n6 = len(arr5)

    k_values = [1, 3, 5]  # Find the 1st, 3rd, and 5th largest elements

    results = {}  # Use a dictionary instead of a list
    for k in k_values:
        k_largest = n6 - k  # Convert to k-th smallest index
        results[k] = quickSelect(arr5[:], 0, n6 - 1, k)  # Corrected function call

    print("\nMultiple k-th largest elements:")
    for k, value in results.items():
        print(f"{k}-th largest element: {value}")

