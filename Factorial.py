class factorial:

    def __init__(self,n):
        self.n=n

    def fact(self):
        f,i=1,self.n
        while i>0:
            f*=i
            i-=1
        return f

n=int(input('Enter any number'))
f1=factorial(n)
print('Factorial=',f1.fact())



