def selection_sort(word):
    n = len(word)
    for i in range(n-1):
        min_pos = i
        for j in range(i+1,n):
            if word[j] < word[min_pos]:
                min_pos = j
        if min_pos != i:
            word[i], word[min_pos] = word[min_pos], word[i]

if __name__ == '__main__':
    word = ["banana", "apple", "cherry", "date"]
    selection_sort(word)
    print(word)