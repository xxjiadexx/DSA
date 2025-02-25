def swap(a,b,arr):
    arr[a] , arr[b] = arr[b], arr[a]

def partition(array,start,end):
    pivot_index = start
    pivot = array[pivot_index]


    while start < end:
        while  start < len(array) and array[start] <= pivot:
            start += 1

        while array[end] > pivot:
            end -= 1

        if start < end:
            swap(start,end,array)

    swap(pivot_index,end,array)

    return end

def quickSort(array,start,end):
    if start < end:
        pi = partition(array,start,end)
        quickSort(array,start,pi-1) # left partition
        quickSort(array,pi+1,end) # right partition

if __name__ == '__main__':
    arr = [ 11,9,29,7,2,15,28]
    quickSort(arr,0,len(arr)-1)
    print(arr)