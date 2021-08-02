n=int(input('Enter number to be reversed'))
m,k=0,n
while n>0:
    r=n%10
    n=int(n/10)
    m=m*10+r
if m==k:
    print('Palindrome')
else:
    print('Not Palindrome')