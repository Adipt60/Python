class evenodd:

    def __init__(self,n):
        self.n = n

    def compare(self):
        if self.n % 2 == 0:
            return 'Even'
        else:
            return 'Odd'

n=int(input('Enter any number'))
a=evenodd(n)
print('The number is ',a.compare())