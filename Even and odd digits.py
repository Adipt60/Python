n=int(input('Enter number n'))
e,o=0,0
while n>0:
    r=n%10
    n=int(n/10)

    if r%2==0:
        e+=1
    else:
        o+=1
print("Even= {}  Odd= {} ".format(e,o))