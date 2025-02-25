def selection_sort(array):
    n = len(array)
    incre = 0
    for i in range(n-1):
        min_pos = i
        for j in range(i+1,n):
            if array[j] < array[min_pos]:
                min_pos = j
        if min_pos != i:
            array[i], array[min_pos] = array[min_pos], array[i]
            incre += 1
    return incre

if __name__ == '__main__':
    number = [4,3,2,1]
    total_swapped = selection_sort(number) 
    print(number)
    print(f'Total Swaps {total_swapped}')