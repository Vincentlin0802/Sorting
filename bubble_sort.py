def bubblesort(arr):
    if len(arr) < 2:
        return arr
    for i in range(len(arr)):
        for j in range(len(arr) - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


if __name__ == '__main__':
    a = [5, 3, 4, 2, 1]
    bubblesort(a)
    print(a)
