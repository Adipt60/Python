class armstrong:

    def __init__(self,n):
        self.n=n

    def check(self):
        m,sum=self.n,0
        while m>0:
            r=m%10
            m=int(m/10)
            sum+=r**3

        if self.n==sum:
            return 'Armstrong Number'
        else:
            return 'Not Armstrong Number'


n=int(input('Enter any number'))
a1=armstrong(n)
print(a1.check())

