def swap(array,start,end):
    array[start], array[end] = array[end],array[start]

def partition(array,start,end):
    pivotIndex = start
    pivotValue = array[pivotIndex]
    n = len(array)

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


def quickSelect(array, start, end,k):
    if start <= end:
        pi = partition(array, start, end)

        if pi == k:
            return array[pi]
        elif pi > k:
            return quickSelect(array, start, pi - 1, k)
        else:
            return quickSelect(array, pi + 1, end, k)

if __name__ == '__main__':
    nums = [10, 7, 8, 9, 1, 5]
    k = 2
    result = quickSelect(nums,0,len(nums)-1,k)
    quickSort(nums,0,len(nums)-1)
    print(result)