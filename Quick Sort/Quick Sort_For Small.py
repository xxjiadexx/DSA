def quickSort(sequence):
    n = len(sequence)

    if n <= 1:
        return sequence
    else:
        pivot = sequence.pop()

    items_greater = []
    items_lower = []

    for item in sequence:
        if item > pivot:
            items_greater.append((item))
        else:
            items_lower.append(item)

    return quickSort(items_lower) + [pivot] + quickSort(items_greater)


if __name__ == '__main__':
    unSorted = [4, 2, 4, 1, 3, 2, 5, 3, 1]
    sorted = quickSort(unSorted)
    print(f'{sorted}')