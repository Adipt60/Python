class fibonacci:

    def __init__(self,n):
        self.n=n

    def series(self):
        print(0,' ',1,' ',end="")
        a,b,i=0,1,0
        while i<(n-2):
            c=a+b
            a,b=b,c
            i+=1
            print(c,' ',end="")

n=int(input('Enter number of terms'))
f=fibonacci(n)
f.series()