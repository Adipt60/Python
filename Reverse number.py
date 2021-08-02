n=int(input('Enter number to be reversed'))
m=0
while n>0:
    r=n%10
    n=int(n/10)
    m=m*10+r
print('Reversed number= ',m)