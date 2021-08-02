from array import *

n=int(input('Enter no. of elements in array'))
print("Enter {} elements".format(n))
ar=array('i',[])
for i in range(n):
    ar.append(int(input()))

def add(x):
    k,sum=len(x),0
    for i in range(k):
        sum+=x[i]
    return sum

print("Sum= ",add(ar))