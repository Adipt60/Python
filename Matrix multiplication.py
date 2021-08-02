from numpy import *
r,c=int(input('Enter no. of rows and columns for 1st matrix')),int(input())
a=zeros([r,c],dtype=int)
print('Enter {} elements in 1st matrix'.format(r*c))

for i in range(r):
    for j in range(c):
        a[i][j]=int(input())
m1=matrix(a)

n=int(input('Enter no. of columns for 2nd matrix'))
b=zeros([c,n],dtype=int)
print('Enter {} elements in 2nd matrix'.format(c*n))

for i in range(c):
    for j in range(n):
        b[i][j]=int(input())
m2=matrix(b)

def prod(x,y):
    (k,l)=x.shape
    (l,m)=y.shape
    z=zeros([k,m],dtype=int)

    for i in range(k):
        for j in range(m):
            for e in range(l):
                z[i][j]+=x[i][e]*y[e][j]

    return z

print(prod(a,b))
print(m1*m2)