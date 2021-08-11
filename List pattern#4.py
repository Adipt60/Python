n=int(input('Enter n'))
for i in range(1,n+1):
    l=[]
    for j in range(n+1):
        l.append(j**i)
    print('Number raised to power {} ==>'.format(i),l)