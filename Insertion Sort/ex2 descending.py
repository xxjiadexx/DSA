def insertion_sort(array):
    n = len(array)
    for i in range(1,n):
        temp = array[i]
        j = i -1


        while j >= 0 and temp > array[j]:
            array[j+1] = array[j]
            j = j -1
        array[j+1] = temp


if __name__ == '__main__':
    arr = [8, 4, 3, 7, 2]
    insertion_sort(arr)
    print(arr)