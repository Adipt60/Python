class product:

    def __init__(self,l):
        self.l=l

    def multiply(self):
        k,p=len(l),1
        for i in range(n):
            p*=l[i]
        return p


n=int(input('Enter number of elements'))
l=[]
print('Enter {} elements'.format(n))
for i in range(n):
    l.append(int(input()))
l1=product(l)
print('Product=',l1.multiply())