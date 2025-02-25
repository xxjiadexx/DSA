def merge_sort(array):
    n = len(array)

    if n <= 1:
        return array

    mid = len(array) // 2
    leftHalf =array[:mid]
    rightHalf = array[mid:]

    sortedLeft = merge_sort(leftHalf)
    sortedRight = merge_sort(rightHalf)

    return merge(sortedLeft,sortedRight)

def merge(left,right):
    result =[]
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[i]:
            result.append(left[i])
            i += 1

        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result



if __name__ == '__main__':
    unsortedArr = [3, 7, 6, -10, 15, 23.5, 55, -13]
    sortedArr = merge_sort(unsortedArr)
    print("Sorted array:", sortedArr)
