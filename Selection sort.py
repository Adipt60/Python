n=int(input('Enter no. of elements in list'))
lst=[]
print('Enter {} elements in list'.format(n))

for i in range(n):
    lst.append(int(input()))

def sort(x):
    for i in range(len(x)-1):
        min=i
        for j in range(i,len(x)):
            if x[min]>x[j]:
                min=j
        x[i],x[min]=x[min],x[i]

    return x

print('Sorted List = ',sort(lst))