def insertionsort(arr):
    if len(arr) < 2:
        return arr
    for i in range(1, len(arr)):
        j = i - 1
        while j >= 0:
            if arr[j] > arr[j + 1]:
               arr[j], arr[j + 1] = arr[j + 1], arr[j]
            elif arr[j] < arr[j + 1]:
                break
            j -= 1
    return arr


if __name__ == '__main__':
    print(insertionsort([1,5,4,2,3]))
