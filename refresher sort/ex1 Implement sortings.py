def bubble_sort(array):
    n = len(array)
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if array[j] > array[j+1]:
                array[j] , array[j+1] = array[j + 1], array[j]
                swapped = True
        if not swapped:
            break

def selection_sort(array):
    n = len(array)
    for i in range(n - 1):
        min_value = i
        for j in range(i+1,n):
            if array[j] < array[min_value]:
                min_value = j
        if min_value != i:
            array[i], array[min_value] = array[min_value], array[i]

def insertion_sort(array):
    n = len(array)
    for i in range(1,n):
        temp = i
        j = i -1

        while j >= 0 and temp<array[j]:
            array[j+1] = array[j]
            j = j -1
        array[j+1] = temp




if __name__ == '__main__':
    list = [64, 34, 25, 12, 22, 11, 90]
    bubble_sort(list)
    selection_sort(list)
    insertion_sort(list)

    print(f'{list}\n')
    print(f'{list}\n')
    print(f'{list}\n')
