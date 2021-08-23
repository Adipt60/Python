n,m=int(input('Enter 2 numbers')),int(input())

def hcf(n,m):
    n,m=n,m
    i=n
    while i>0:
        if n%i==0:
            j=m
            while j>0:
                if m%j==0:
                    if i==j:
                        return i
                    else:
                        pass
                else:
                    pass
                j-=1
        else:
            pass
        i-=1

def lcf(n,m):
    n,m=n,m
    i=2
    while i<=n:
        if n%i==0:
            j=2
            while j<=m:
                if m%j==0:
                    if i==j:
                        return i
                    else:
                        pass
                else:
                    pass
                j+=1
        else:
            pass
        i+=1

print('HCF = ',hcf(n,m))
print('LCF = ',lcf(n,m))