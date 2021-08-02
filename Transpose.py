from numpy import *
r,c=int(input('Enter no. of rows and columns')),int(input())
a=zeros([r,c],dtype=int)
print('Enter {} elements in matrix'.format(r*c))

for i in range(r):
    for j in range(c):
        a[i][j]=int(input())

m=matrix(a)

def transpose(x):
    (k,l)=x.shape
    z=zeros([k,l],dtype=int)

    for i in range(k):
        for j in range(l):
            z[i][j]=x[j][i]
    return z

print(transpose(a))