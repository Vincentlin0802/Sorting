def bubblesort(list):
    for i in range(len(list)):
        for i in range(0, len(list) - 1):
            if len(list) < 2:
                print(list)
                break
            elif list[i] > list[i + 1]:
                list[i], list[i + 1] = list[i + 1],list[i]
if __name__ == '__main__':
    list = [5, 3, 4, 2, 1]
    bubblesort(list)
    print(list)
