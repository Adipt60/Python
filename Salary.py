class salary:

    def __init__(self,n):
        self.n=n
        self.hra,self.ta,self.tax=(10/100)*self.n,(5/100)*self.n,(2/100)*self.n


    def gross(self):
        gs = self.n + self.hra + self.ta
        return gs

    def net(self):
        net = self.gross()-self.tax
        return net

n=float(input('Enter Basic Salary'))
s1=salary(n)
print('Gross Salary = ',s1.gross())
print('Net Salary = ',s1.net())
