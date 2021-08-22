def add():
    x,y=float(input('Enter 2 numbers to be added')),float(input())
    return x+y

def sub():
    x, y = float(input('Enter 2 numbers to be subtracted in order')), float(input())
    return x-y

def mul():
    x, y = float(input('Enter 2 numbers to be multiplied')), float(input())
    return x*y

def div():
    x, y = float(input('Enter 2 numbers to be divided in order')), float(input())
    return x/y

def pow():
    x, y = float(input('Enter base')), float(input('Enter power'))
    return x**y

def fac():
    x = int(input('Enter number'))
    f=1
    while x>0:
        f*=x
        x-=1
    return f

def error():
    return 'Invalid choice'


print('''
    1.Add
    2.Subtract
    3.Multiply
    4.Divide
    5.Power
    6.Factorial
''')

choice=int(input('Choose from the above'))

options={
    1:add,
    2:sub,
    3:mul,
    4:div,
    5:pow,
    6:fac
}

print(options.get(choice,error)())