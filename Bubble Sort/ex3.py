def bubble_sort(students):
    n = len(students)
    for i in range(n-1):
        swapped = False
        for j in range (n-1-i):
            if students[j][1] > students[j + 1][1]:
                students[j], students[j + 1] = students[j + 1], students[j]
                swapped = True
        if not swapped:
            break

if __name__ == '__main__':
    students = [("Alice", 88), ("Bob", 75), ("Charlie", 95), ("David", 60)]
    bubble_sort(students)
    print(students)

