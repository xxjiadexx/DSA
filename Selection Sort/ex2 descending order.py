def selection_sort(array):
    n = len(array)
    for i in range(n-1):
        min_pos = i
        for j in range(i+1,n):
            if array[j] > array[min_pos]:
                min_pos = j
        if min_pos != i:
            array[i], array[min_pos] = array[min_pos],array[i]


if __name__ == '__main__':
    number = [5, 2, 9, 1, 5, 6]
    selection_sort(number)
    print(number)