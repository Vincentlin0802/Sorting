def mergesort(arr):
    if len(arr) <= 1:
        return arr
    middle = len(arr) // 2
    left = mergesort(arr[:middle])
    right = mergesort(arr[middle:])
    arr2 = []
    p1 = 0
    p2 = 0
    while p1 < len(left) and p2 < len(right):
        if left[p1] < right[p2]:
            arr2.append(left[p1])
            p1 += 1
        else:
            arr2.append(right[p2])
            p2 += 1

    if p1 == len(left):
        arr2.extend(right[p2:])
    else:
        arr2.extend(left[p1:])

    return arr2


if __name__ == '__main__':
    a = [1,5,4,2,3]
    print(mergesort(a))
