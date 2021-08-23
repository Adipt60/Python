n=int(input('Enter number of values to be entered'))
l,e,o=[],[],[]
print('Enter {} values into list'.format(n))
for i in range(n):
    l.append(int(input()))

for i in l:
    if i%2==0:
        e.append(i)
    else:
        o.append(i)

print(l)
l=[e,o]
print(l)