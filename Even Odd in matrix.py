from numpy import *
r,c=int(input('Enter no. of rows and columns')),int(input())
a=zeros([r,c],dtype=int)
print('Enter {} elements in matrix'.format(r*c))

for i in range(r):
    for j in range(c):
        a[i][j]=int(input())

m=matrix(a)

def eo(x):
    e,o=0,0
    for i in x:
        for j in i:
            if j%2==0:
                e+=1
            else:
                o+=1
    return e,o

print('Even= {}  Odd= {}'.format(eo(a)[0],eo(a)[1]))