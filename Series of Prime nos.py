import math as m
n=int(input('Enter n'))
k,j=2,0
while j<n:
    bool, i = 0, 2
    while i < k:
        if k % i == 0:
            bool = True
            break
        else:
            bool = False
        i += 1
    if bool == True:
        pass
    else:
        print(k,'',end="")
        j += 1
    k+=1





























