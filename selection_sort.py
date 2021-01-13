def selectionsort(arr):
    if len(arr) < 2:
        return arr
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


if __name__ == '__main__':
    a = [5, 3, 4, 2, 1]
    print(selectionsort(a))
