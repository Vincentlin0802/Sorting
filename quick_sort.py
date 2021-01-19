def partition(arr,left,right):
    pivot = arr[right]     #把数组的最后一个数当作基准
    for l in range(left-1, len(arr)):
        for j in range(left,right): #从左到右开始遍历
            if arr[j] <= pivot:
                l = l+1             #如果这个数小于基准 那么就将小于的部分扩大，然后继续遍历
                arr[l], arr[j] = arr[j], arr[l]  #将小于基准的数都放到数组左边
        arr[l+1],arr[right] = arr[right], arr[l+1]
        return(l+1)

def quicksort(arr,left, right):
    if left < right:
        k = partition(arr,left,right)  #找出中间相等于基准的index
        print(k)
        (quicksort(arr,left,k-1))   #数组排好的的左边部分继续进行递归
        (quicksort(arr,k+1,right))  #数组排好的右边部分继续进行递归
        return arr
if __name__ == '__main__':
     a = [1,5,4,6,2,3]
     print(quicksort(a,0,len(a)-1))



