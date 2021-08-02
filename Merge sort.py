from array import *

n=int(input('Enter number of elements in 1st array'))
a=array('i',[])
print('Enter {} elements in sorted form'.format(n))
for i in range(n):
    a.append(int(input()))

m=int(input('Enter number of elements in 2nd array'))
b=array('i',[])
print('Enter {} elements in sorted form'.format(m))
for i in range(m):
    b.append(int(input()))

def merge(x,y):
    c=array('i',[])
    k,l=len(x),len(y)
    i,j=0,0
    while i<k and j<l:
        if x[i]<=y[j]:
            c.append(x[i])
            i+=1
        else:
            c.append(y[j])
            j+=1

    while i<k:
        c.append(x[i])
        i+=1

    while j<l:
        c.append(y[j])
        j+=1

    return c



print('Merged array= ',merge(a,b))
