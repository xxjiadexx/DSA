def mergeSort(array):
    n = len(array)
    if n <= 1:
        return array

    mid = n // 2
    leftHalf = array[:mid]
    rightHalf = array[mid:]

    leftSorted = mergeSort(leftHalf)
    rightSorted = mergeSort(rightHalf)

    return merge(leftSorted,rightSorted)

def merge(left,right):
    result = []
    i = j = 0
    nl = len(left)
    nr = len(right)

    while i < nl and j < nr:
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])

    return result



if __name__ == '__main__':
    unSorted = [4, 2, 4, 1, 3, 2, 5, 3, 1]
    sorted = mergeSort(unSorted)
    print(f'{sorted}')