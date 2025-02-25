def bubble_sort(people, key= None):
    n = len(people)
    for i in range(n-1):
        swapped = False
        for j in range(n-1-i):
            a = people[j][key]
            b = people[j+1][key]
            if a > b:
                people[j], people[j+1] = people[j+1],people[j]
                swapped = True
        if not swapped:
            break


if __name__ == '__main__':
    people = [
        {"name": "Alice", "age": 25},
        {"name": "Bob", "age": 30},
        {"name": "Charlie", "age": 22}
    ]
    bubble_sort(people,key='age')
    print(people)