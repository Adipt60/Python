class list:

    def __init__(self,l):
        self.l=l

    def sm(self):
        s=sum(self.l)
        return s

    def avg(self):
        a=self.sm()/len(self.l)
        return a

    def maximum(self):
        mx=max(self.l)
        return mx

    def minimum(self):
        mn=min(self.l)
        return mn


l=[]
N=int(input('Enter number of values to be entered'))
print('Enter {} values in list'.format(N))
for i in range(N):
    l.append(float(input()))

l1=list(l)
print('Maximum = ',l1.maximum())
print('Minimum = ',l1.minimum())
print('Sum = ',l1.sm())
print('Average = ',l1.avg())