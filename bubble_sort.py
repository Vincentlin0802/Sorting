def bubblesort(list):
    for i in range(len(list)):
        for j in range(0, len(list) - 1):
            if len(list) < 2:
                 break
            elif list[j] > list[j + 1]:
                 list[j], list[j + 1] = list[j + 1], list[j]

    return list


if __name__ == '__main__':
    a = [5,3,4,2,1]
    bubblesort(a)
    print(a)
