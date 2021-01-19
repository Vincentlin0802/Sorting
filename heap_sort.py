def heapify(arr,heapsize,i):
    largest = i     #父节点
    left = 2*i+1   #左节点
    right = 2*i+2  #右节点
    if left < heapsize and arr[i] < arr[left]:   #如果左节点不越界，并且左节点大于父节点，那么赋值给largest
        largest = left
    if right < heapsize and arr[largest] < arr[right]: #继续比较大小
        largest = right
    if largest != i:                         #将最大的数置于堆的顶端(数组的最前面)
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, heapsize, largest)

def heapsort(arr):
    heapsize = len(arr)
    for i in range(heapsize,-1,-1):     #建立大根堆，满足完全二叉树
        heapify(arr,heapsize,i)
    for i in range(heapsize-1,0,-1):
        arr[i] ,arr[0] = arr[0], arr[i]     #将最大的数放到数组的最后
        heapify(arr,i,0)
    return arr

if __name__ == '__main__':
     a = [1,5,4,6,2,3]
     print(heapsort(a))