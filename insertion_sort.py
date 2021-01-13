def insertionsort(list):
    for i in range(1, len(list)):
        j = i - 1
        while j >= 0:
            if len(list) < 2:
                break
            elif list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
            j -= 1
    return list


if __name__ == '__main__':
    print(insertionsort([5, 3, 4, 2, 1]))
