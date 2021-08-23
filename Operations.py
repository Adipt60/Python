n=int(input('Enter any number'))

print(n**0.5)
print(n**2)
print(n**3)

def prime(n):
    global bool
    if n==2:
        return 'Prime'
    else:
        i,n=2,n
        while i<n:
            if n%i==0:
                bool=False
                return 'Not Prime'
            else:
                bool=True
            i+=1
        if bool:
            return 'Prime'


def fact(n):
    n,f=n,1
    for i in range(1,n+1):
        f*=i
    return f

def primefact(n):
    n,i=n,2
    while i<=n:
        if n%i==0:
            if prime(i)=='Prime':
                print(i,' ',end="")
        else:
            pass
        i+=1


print(prime(n))
print(fact(n))
primefact(n)




