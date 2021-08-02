from math import *
n = int(input('Enter number of terms'))
y = float(input('Enter angle in degrees'))
x = (y*pi)/180

def sine(a):
    sum,k,c= 0,1,1
    for i in range(n):
        sum += (pow(a,k)*c)/factorial(k)
        k += 2
        c = -c
    return sum

def factorial(b):
    f = 1
    for i in range(1,b+1):
        f*=i

    return f

print("Sin({}) = ".format(x),sine(x))