n=int(input('Enter number to be checked'))
m,k=0,n
while n>0:
    r=n%10
    n=int(n/10)
    m+=r**3
if m==k:
    print('Armstrong')
else:
    print('Not Armstrong')