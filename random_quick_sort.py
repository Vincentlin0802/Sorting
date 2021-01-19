import random
def partition(arr,left,right):
    pivot_index = random.randint(left,right)   #在数组中随机生成一个数
    arr[right], arr[pivot_index] = arr[pivot_index],arr[right]  #将生成的数和数组最后的一个数互换
    pivot = arr[right]
    for l in range(left-1, len(arr)):
        for j in range(left,right):
            if arr[j] <= pivot:
                l = l+1
                arr[l], arr[j] = arr[j], arr[l]
        arr[l+1],arr[right] = arr[right], arr[l+1]
        return(l+1)

def quicksort(arr,left, right):
    if left < right:
        k = partition(arr,left,right)
        print(k)
        (quicksort(arr,left,k-1))
        (quicksort(arr,k+1,right))
        return arr
if __name__ == '__main__':
     a = [1,5,4,6,2,3]
     print(quicksort(a,0,len(a)-1))