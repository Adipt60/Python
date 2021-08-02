from array import *
n=int(input('Enter number of elements'))
ar=array('i',[])
print('Enter {} elements'.format(n))

for i in range(n):
    ar.append(int(input()))

def prod(x):
    k,pr=len(x),1
    for i in range(k):
        pr*= x[i]
    return pr

print('Product= ',prod(ar))