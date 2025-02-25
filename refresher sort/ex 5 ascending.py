def bubble_sort(array):
    n = len(array)
    for i in range(n-1):
        swapped = False
        for j in range(n-1-i):
            if array[j] > array[j+1]:
                array[j] , array[j+1] = array[j+1], array[j]
                swapped = True
        if not swapped:
            break

def selection_sort(array):
    n = len(array)
    for i in range(n-1):
        min_pos = i
        for j in range(i+1,n):
            if array[j] < array[min_pos]:
                min_pos = j
        if min_pos != i:
            array[i], array[min_pos] = array[min_pos], array[i]

def insertion_sort(array):
    n = len(array)
    for i in range(1,n):
        val = array[i]
        j = i - 1
        while j >= 0 and val<array[j]:
            array[j+1] = array[j]
            j = j - 1

        array[j+1] = val

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
    i = j = 0
    nl = len(left)
    nr = len(right)


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






if __name__ == '__main__':
    test = [2, 1, 3, 4, 5, 6, 7, 8, 9]
    bubble_list = test.copy()
    selection_list = test.copy()
    insertion_list = test.copy()
    merge_list = test.copy()

    bubble_sort(bubble_list)  # Sorts in-place
    selection_sort(selection_list)  # Sorts in-place
    insertion_sort(insertion_list)  # Sorts in-place
    merge_list = mergeSort(merge_list)  # mergeSort returns a new list

    print(f'Bubble Sort: {bubble_list}')
    print(f'Selection Sort: {selection_list}')
    print(f'Insertion Sort: {insertion_list}')
    print(f'Merge Sort: {merge_list}')