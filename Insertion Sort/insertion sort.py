def insertion_sort(number):
    n = len(number)
    for i in range(1,n):
        key = number[i]
        j = i-1
        while j >= 0 and key<number[j]:
            number[j+1] = number[j] ## Shifting
            j = j -1
        number[j+1] = key


if __name__ == '__main__':
    number = [7,11,3,1,2,5,6,9]
    insertion_sort(number)
    print(number)