class result:

    def __init__(self,l):
        self.l=l

    def aggregate(self):
        ag=(sum(self.l)/500)*100
        return ag

    def calresult(self):

        if min(self.l)<40 or self.aggregate()<40:
            return 'FAILED'
        elif self.aggregate()>=75:
            return 'PASSED with Distinction'
        elif 60<=self.aggregate()<75:
            return 'PASSED in First Division'
        elif 50<=self.aggregate()<60:
            return 'PASSED in Second Division'
        else:
            return 'PASSED in Third Division'



l=[]
print('Enter marks in 5 courses')
for i in range(5):
    l.append(float(input()))

r1=result(l)
print(r1.calresult())

