def insertion_sort(number):
    n = len(number)
    for i in range(1,n):
        temp = number[i]
        j = i - 1

        while j >= 0 and temp < number[j]:
            number[j+1] = number[j]
            j -= 1
        number[j+1] = temp


if __name__ == '__main__':
    number = [12, 11, 13, 5, 6]
    insertion_sort(number)
    print(number)