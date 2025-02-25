def swap(array,start,end):
    array[start], array[end] = array[end],array[start]

def bubbleSort(array):
    n =len(array)
    for i in range(n-1):
        swapped = False
        for j in range(n-1-i):
            if array[j] > array[j+1]:
                swap(array,j,j+1)
                swapped = True
        if not swapped:
            break

def selectionSort(array):
    n = len(array)
    for i in range(n-1):
        minPos = i
        for j in range(i+1,n):
            if array[j] < array[minPos]:
                minPos = j
        if minPos != i :
            swap(array,i,minPos)

def insertionSort(array):
    n = len(array)
    for i in range(1,n):
        temp = array[i]
        j = i - 1
        while j >= 0 and temp > array[j]:
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

    leftsort = mergeSort(leftHalf)
    rightsort = mergeSort(rightHalf)

    return merge(leftsort,rightsort)

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
    pivotIndex = start
    pivotVal = array[pivotIndex]
    n = len(array)

    while start < end:
        while start < n and array[start] <= pivotVal:
            start += 1
        while array[end] > pivotVal:
            end -= 1
        if start < end:
            swap(array,start,end)
    swap(array,pivotIndex,end)
    return end

def quickSort(array,start,end):
    if start < end:
        pi = partition(array,start,end)
        quickSort(array,start,pi-1)
        quickSort(array,pi+1,start)
    return array

if __name__ == '__main__':
    bub = [29, 10, 14, 37, 13]
    bubbleSort(bub)
    print(f'Bubble Sort: {bub}')

    scores = [85, 72, 90, 67, 88, 79]
    selectionSort(scores)
    print(f'Selection Sort: {scores}')

    arr = [5,3,8,1,2]
    insertionSort(arr)
    print(f'Insertion sorted: {arr}')

    alpha = ["banana", "apple", "cherry", "date"]
    mergeSorted = mergeSort(alpha)
    print(f'Merge Sort: {mergeSorted}')

    nums = [7, 2, 1, 6, 8, 5, 3, 4]
    sorted = quickSort(nums,0,len(nums)-1)
    print(f'Quick Sort {sorted}')