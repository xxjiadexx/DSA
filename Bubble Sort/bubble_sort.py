def bubble_sort(array):
    n  = len(array)
    for i in range(n-1):
        swapped = False
        for j in range(n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                swapped = True
        if not swapped:
            break




if __name__ == '__main__':
    array = [ 1,200,100,123,80,99,310,201,122]

    bubble_sort(array)
    print(array)

