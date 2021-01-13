def mergesort(list):

    if len(list) <= 1:
        return list
    middle = len(list) // 2
    left = mergesort(list[:middle])
    right = mergesort(list[middle:])
    list2 = []
    p1 = 0
    p2 = 0
    while p1 < len(left) and p2 < len(right):
        if left[p1] < right[p2]:
            list2.append(left[p1])
            p1 += 1
        else:
            list2.append(right[p2])
            p2 += 1

    if p1 == len(left):
         list2.extend(right[p2:])
    else:
         list2.extend(left[p1:])

    return list2


if __name__ == '__main__':
    a = [5,4,3,2,1]
    print(mergesort(a))
