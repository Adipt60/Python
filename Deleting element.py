from array import *
ar=array('i',[])
n=int(input('Enter no of elements in array'))

print('Enter ',n,' values in the array')


for i in range(0,n):
    ar.append(int(input()))

a=int(input('Enter element to be deleted'))
ar.remove(a)

for i in range(0,n-1):
    print(ar[i])




