n=int(input('Enter binary number'))
i,sum=0,0
while n>0:
    r=n%10
    n=int(n/10)
    sum+= r*(2**i)
    i+=1

print(sum)