import random
def rearrange(arr,left,right):
   for i in range(0,len(arr),1):
        num = random.randint(left,right)
        arr.append(num)
        arr.remove(num)
   return arr

if __name__ == '__main__':
     a = [1,2,3,4,5,6]
     print(rearrange(a,a[0],a[len(a)-1]))