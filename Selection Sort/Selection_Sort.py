def selection_sort(array):
    n = len(array)
    for i in range(n-1):
        min_index = i
        for j in range(i+1,n):
            if array[j] < array[min_index]:
                min_index = j
        if min_index != i:
            array[i], array[min_index] = array[min_index], array[i]

if __name__ == '__main__':
    number = [7,12,9,11,33]
    selection_sort(number)
    print(number)