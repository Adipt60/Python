class momentum:

    def __init__(self,m,c):
        self.m = m
        self.c = c

    def calculate(self):
        e = self.m * (self.c ** 2)
        return e
m , c = float(input('Enter mass in kilograms')) , float(input('Enter velocity in meters per second'))
m1 = momentum(m,c)
print('Momentum = ',m1.calculate(),'kg.m/s')