count = {}

# Swap elements at index i and j in array a
def swap(a, i, j):
    global count
    a[i], a[j] = a[j], a[i]  # Swap elements

    count[a[i]] = count[a[i]] + 1
    count[a[j]] = count[a[j]] + 1

# Implement bubble sort using swap()
def bubbleSort(a):
    n = len(a)
    for i in range(n-1):
        swapped = False
        for j in range(n-1-i):
            if a[j] > a[j+1]:
                swap(a,j,j+1)
                swapped = True
        if not swapped:
            break

# Get user input
array = input("Enter a list of strings to sort, separated by commas:\n")
array = [str(x) for x in array.split(",")]

# Set up the dictionary to track counts
for x in array:
    count[x] = 0

bubbleSort(array)

# Print results
print("Sorted list:", array)
print("Number of swaps for each item:", count)

total = sum(count.values())
print("Average number of swaps per item:", total / len(count))
