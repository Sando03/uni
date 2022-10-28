def plus(a,b):
    print(a+b)
def minus(a,b):
    print(a-b)
def multiply(a,b):
    print(a*b)
def divide(a,b):
    print(a/b)
a=int(input('a= '))
b=int(input('b= '))
oper = str(input('Enter operation +,-,*,/ '))
if oper =='+':
    plus(a,b)
elif oper =='-':
    minus(a,b)
elif oper =='*':
    multiply(a,b)
elif oper =='/':
    divide(a,b)