
n=int(input('Enter Number till where sum is to be found'))
sum=0
def factorial(b):
    f = 1
    for i in range(1,b+1):
        f*=i
    return f


for i in range(n+1):
    sum+=factorial(i)
print("Sum= ",sum)



