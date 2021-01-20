import random
def rearrange(arr):
   for i in range(0,len(arr)):
        num = random.randint(0, len(arr)-1)
        arr[i],arr[num] = arr[num], arr[i]
   return arr

def proveleft(arr):
   middle = len(arr) // 2
   n1 = 0
   for j in range(0,middle):
       n1 = arr[j] + n1
   n1 = n1 // middle
   return n1

def proveright(arr):
    middle = len(arr) // 2
    n2 = 0
    for k in range(middle, len(arr)):
        n2 = arr[k] + n2
    n2 = n2 // middle
    return n2

if __name__ == '__main__':
     a = [1,2,3,4,5,6]
     print(rearrange(a))
     print("左边平均值:", proveleft(a))
     print("右边平均值:", proveright(a))