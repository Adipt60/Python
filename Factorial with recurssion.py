n=int(input('Enter a number'))
def factorial(x):
    if x==0:
        return 1
    else:
        f=x*factorial(x-1)
        return f

print(factorial(n))