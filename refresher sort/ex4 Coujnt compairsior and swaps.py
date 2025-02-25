def bubble_sort(array):
    n = len(array)
    comparisons = 0
    swaps = 0
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            comparisons += 1  # Count comparison
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]  # Swap
                swaps += 1  # Count swap
                swapped = True
        if not swapped:
            break  # Stop early if sorted
    return comparisons, swaps


def selection_sort(array):
    pass

def insertion_sort(array):
    pass



if __name__ == '__main__':
    list = ["banana", "apple", "cherry", "date"]
    bubble_list = list.copy()  # Create a copy for Bubble Sort
    selection_list = list.copy()  # Create a copy for Selection Sort
    insertion_list = list.copy()  # Create a copy for Insertion Sort

    bubble_sort(bubble_list)
    selection_sort(selection_list)
    insertion_sort(insertion_list)

    print(f'Bubble Sort: {bubble_list} Count: {cnt} ')
    print(f'Selection Sort: {selection_list}')
    print(f'Insertion Sort: {insertion_list}')