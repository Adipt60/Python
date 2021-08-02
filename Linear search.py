n=int(input('Enter no. of elements in list'))
lst=[]
print('Enter {} elements in list'.format(n))

for i in range(n):
    lst.append(int(input()))

m=int(input('Enter element to be searched'))

def lsearch(x,k):
    l=len(x)
    for i in x:
        if i==k:
            l=i
            break
        else:
            l=len(x)

    if l!=len(x):
        print('Found at pos = ',x.index(l)+1)
    else:
        print('Not Found')
lsearch(lst,m)