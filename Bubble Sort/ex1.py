def bubble_sort(numbers, key=None):
    n = len(numbers)
    for i in range(n-1):
        swapped = False
        for j in range(n-1-i):
            if numbers[j] > numbers[j+1]:
                numbers[j],numbers[j+1] = numbers[j+1], numbers[j]
                swapped = True
        if not swapped:
            break


if __name__ == '__main__':
    numbers = [64, 34, 25, 12, 22, 11, 90]
    bubble_sort(numbers)
    print(f'Sorted: {numbers}\n')


