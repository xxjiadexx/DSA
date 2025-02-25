def bubble_sort(numbers):
    n = len(numbers)
    count = 0  # Initialize swap count
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            count += 1  # Increment count for each comparison
            if numbers[j] > numbers[j + 1]:  # Sorting in descending order
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
                swapped = True
        if not swapped:
            break
    return count  # Return the swap count


if __name__ == '__main__':
    numbers = [3, 2, 1]
    swap_count = bubble_sort(numbers)  # Store the returned count
    print(numbers)  # Expected output: [3, 2, 1] (already sorted)
    print(f'Number of Swaps: {swap_count}')
