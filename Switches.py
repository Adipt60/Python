class switches:

    def __init__(self,n):
        self.n=n

    def number(self):
        r = 2**self.n
        return r

n=int(input('Enter number of switches'))
s1 = switches(n)
print('No of outcomes = ',s1.number())