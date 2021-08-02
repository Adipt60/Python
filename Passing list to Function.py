lst=[]
print('Enter 10 names')

for i in range(10):
    lst.append(input())

def count(x):
    c=0
    for i in x:
        if len(i)>5:
            c+=1
        else:
            pass
    return c

print(count(lst))