def bubble_sort(s):
    n = int(len(name))
    for i in range(n-1):
        swapped = False
        for j in range(n-1-i):
            if name[j] > name[j+1]:
                name[j],name[j+1] = name[j+1], name[j]
                swapped = True
        if not swapped:
            break

if __name__ == '__main__':
    name = input('Enter your name:')
    bubble_sort(name)
    print(name)