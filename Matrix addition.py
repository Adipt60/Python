from numpy import *
r,c=int(input('Enter no. of rows and columns')),int(input())
a=zeros([r,c],dtype=int)
print('Enter {} elements in matrix'.format(r*c))

for i in range(r):
    for j in range(c):
        a[i][j]=int(input())

m=matrix(a)

def add(x):
    s=0
    for i in x:
        for j in i:
           s+=j
    return s


print('Sum= ',add(a))