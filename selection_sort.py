def selectionsort(list):
    list2 = []
    i = 0
    j = len(list)
    while i < j:
        a = min(list)
        list.remove(a)
        list2.append(a)
        i += 1
    return list2


if __name__ == '__main__':
    print(selectionsort([5, 3, 4, 2, 1]))
