def swap(array,start,end):
    array[start], array[end] = array[end],array[start]

def partition(array,start,end):
    piviotIndex = start
    piviotValue = array[piviotIndex]
    n = len(array)

    while start < end:

        while start < n and array[start] >= piviotValue:
            start += 1

        while array[end] < piviotValue:
            end -= 1

        if start < end:
            swap(array,start,end)

    swap(array,piviotIndex,end)
    return end

def quickSort(array,start,end):
    if start < end:
        pi = partition(array,start,end)
        quickSort(array,start,pi-1)
        quickSort(array,pi+1,end)



def sort_multiple_arrays(arrays):
    for array in arrays:
        quickSort(array, 0, len(array) - 1)
        print(array)


if __name__ == '__main__':
    arrays = [
        [12, 4, 7, 9, 3, 5],
        [6, 1, 3, 5, 4, 2],
        [15, 8, 4, 3, 10],
        [11, 9, 29, 7, 2, 15, 28]
    ]

    sort_multiple_arrays(arrays)