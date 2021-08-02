from numpy import *
r,c=int(input('Enter no. of rows and columns')),int(input())
a=zeros([r,c],dtype=int)
print('Enter {} elements in 1st matrix'.format(r*c))

for i in range(r):
    for j in range(c):
        a[i][j]=int(input())
m1=matrix(a)

from numpy import *
b=zeros([r,c],dtype=int)
print('Enter {} elements in 2nd matrix'.format(r*c))

for i in range(r):
    for j in range(c):
        b[i][j]=int(input())
m2=matrix(b)

def add(x,y):
    (k,l)=x.shape
    z=zeros([k,l],dtype=int)
    
    for i in range(k):
        for j in range(l):
            z[i][j]=x[i][j]+y[i][j]

    return z

print(add(a,b))
print(m1+m2)