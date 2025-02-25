def bubble_sort(numbers):
    n = len(numbers)
    for i in range(n-1):
        swapped = False
        for j in range(n-1-i):
            if numbers[j] < numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
                swapped = True
        if not swapped:
            break

if __name__ == '__main__':
    numbers = [3, 1, 4, 1, 5, 9, 2]
    bubble_sort(numbers)
    print(numbers)