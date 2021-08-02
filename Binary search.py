n=int(input('Enter no. of elements in list'))
lst=[]
print('Enter {} elements in list in sorted form'.format(n))

for i in range(n):
    lst.append(int(input()))

m=int(input('Enter element to be searched'))

def bsearch(x,k):
    low,high=0,len(x)-1,
    l=len(x)
    while low<=high:
        mid=int((low+high)/2)
        if x[mid]==k:
            l=mid
            break
        elif x[mid]<k:
            low=mid+1
        else:
            high=mid-1

    if l!=len(x):
        print('Found at pos = ', l + 1)
    else:
        print('Not Found')


bsearch(lst, m)
