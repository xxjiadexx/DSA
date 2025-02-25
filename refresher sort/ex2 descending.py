def bubble_sort(array):
    n = len(array)
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if array[j] < array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                swapped = True
        if not swapped:
            break

def selection_sort(array):
    n = len(array)
    for i in range(n -1):
        pos = i
        for j in range(i + 1, n):
            if array[j] > array[pos]:
                pos = j
        if pos != i:
            array[i], array[pos] = array[pos], array[i]

def insertion_sort(array):
    n = len(array)
    for i in range(1,n):
        val = array[i]
        j = i - 1
        while j >= 0 and val>array[j]:
            array[j+1] = array[j]
            j = j -1
        array[j+1] = val


if __name__ == '__main__':
    list = [3, 1, 4, 1, 5, 9, 2]
    bubble_list = list.copy()  # Create a copy for Bubble Sort
    selection_list = list.copy()  # Create a copy for Selection Sort
    insertion_list = list.copy()  # Create a copy for Insertion Sort

    bubble_sort(bubble_list)
    selection_sort(selection_list)
    insertion_sort(insertion_list)

    print(f'Bubble Sort: {bubble_list}')
    print(f'Selection Sort: {selection_list}')
    print(f'Insertion Sort: {insertion_list}')