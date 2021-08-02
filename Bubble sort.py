n=int(input('Enter no. of elements in list'))
lst=[]
print('Enter {} elements in list'.format(n))

for i in range(n):
    lst.append(int(input()))



def sort(x):
    for i in range(len(x)-1,0,-1):
        for j in range(i):
            if x[j]>x[j+1]:
                x[j],x[j+1]=x[j+1],x[j]
    return x

print('Sorted List = ',sort(lst))