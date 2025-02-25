def insertion_sort(array):
    n = len(array)
    shifting = 0
    for i in range(1,n):
        temp = array[i]
        j = i -1

        while j>=0 and temp < array[j]:
            array[j+1] = array[j]
            j = j - 1
            shifting = shifting + 1
        array[j+1] = temp
    return shifting


if __name__ == '__main__':
    arr = [4, 3, 2, 1]
    shifting = insertion_sort(arr)
    print(arr)
    print(shifting)