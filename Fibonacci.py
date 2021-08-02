n=int(input("Enter till where should the series be printed"))
a,b,c=0,1,0
print(a)
print(b)
while c<n:
    c=a+b
    a,b=b,c
    if c<n:
        print(c)
    else:
        pass

