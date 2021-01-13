def swapposition(list, p1, p2):
    list[p1], list[p2] = list[p2], list[p1]
    return list

def insertionsort(list):
        for i in range(1,len(list)):
            j=i-1
            while j>=0:
                if len(list) < 2:
                    print(list)
                    break
                elif list[j]>list[j+1]:
                    p1, p2 = j, j+1
                    print(swapposition(list, p1, p2))
                j -= 1

if __name__ == '__main__':
    insertionsort([5, 3, 4, 2, 1])
