import random
def rearrange(arr):
   for i in range(0,len(arr),1):
        num = random.randint(0, len(arr)-1)
        arr[i],arr[num] = arr[num], arr[i]
   return arr

if __name__ == '__main__':
     a = [1,2,3,4,5,6]
     print(rearrange(a))