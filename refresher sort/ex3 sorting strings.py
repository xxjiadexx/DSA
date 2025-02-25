def bubble_sort(array):
    n = len(array)
    for i in range(n-1):
        swapped = False
        for j in range(n - 1 - i):
            if array[j] > array[j+1]:
                array[j],array[j+1] = array[j+1], array[j]
                swapped = True
        if not swapped:
            break

def selection_sort(array):
    n = len(array)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1,n):
            if array[j] > array[min_index]:
                min_index = j
        if min_index != i:
            array[i], array[min_index] = array[min_index], array[i]

def insertion_sort(array):
    n = len(array)
    for i in range(1,n):
        temp = array[i]
        j = i - 1

        while j>= 0 and temp<array[j]:
            array[j+1] = array[j]
            j = j - 1
        array[j + 1] = temp



if __name__ == '__main__':
    list = ["banana", "apple", "cherry", "date"]
    bubble_list = list.copy()  # Create a copy for Bubble Sort
    selection_list = list.copy()  # Create a copy for Selection Sort
    insertion_list = list.copy()  # Create a copy for Insertion Sort

    bubble_sort(bubble_list)
    selection_sort(selection_list)
    insertion_sort(insertion_list)

    print(f'Bubble Sort: {bubble_list}')
    print(f'Selection Sort: {selection_list}')
    print(f'Insertion Sort: {insertion_list}')