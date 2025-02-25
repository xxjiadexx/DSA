import random

def swap(array,start,end):
    array[start], array[end] = array[end], array[start]

def insertionSort(array):
    n = len(array)
    for i in range(1,n):
        temp = array[i]
        j = i - 1
        while j >= 0 and temp < array[j]:
            array[j+1] = array[j]
            j -= 1
        array[j+1] = temp

def mergeSort(array):
    n = len(array)
    if n <= 1:
        return array

    mid = n // 2
    leftHalf = array[:mid]
    rightHalf = array[mid:]

    leftSort = mergeSort(leftHalf)
    rightSort = mergeSort(rightHalf)

    return merge(leftSort,rightSort)

def merge(left,right):
    result = []
    nl = len(left)
    nr = len(right)
    i = j = 0

    while i < nl and j < nr:
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result

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


if __name__ == '__main__':
    arr1 = [34, 7, 23, 32, 5, 62, 32, 78, 12, 9, 54, 21, 45, 37, 8]
    arr2 = [93, 27, 65, 18, 50, 33, 99, 10, 73, 22, 87, 41, 3, 69, 90, 44, 57, 80, 29, 14]
    arr3 = [random.randint(0, 9999) for _ in range(10000)]

    # Insertion Sort (modifies the array in place)
    insertionSort(arr1)
    insertionSort(arr2)
    insertionSort(arr3)
    print(f'Insertion Sort 1: {arr1}')
    print(f'Insertion Sort 2: {arr2}')
    print(f'Insertion Sort 3: {arr3[:10]} ... (truncated)\n')

    # Merge Sort (returns a new sorted list)
    merged1 = mergeSort(arr1[:])  # Copy to avoid modifying original
    merged2 = mergeSort(arr2[:])
    merged3 = mergeSort(arr3[:])

    print(f'Merge Sort 1: {merged1}\n')
    print(f'Merge Sort 2: {merged2}\n')
    print(f'Merge Sort 3: {merged3[:10]} ... (truncated)\n')

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