import math
def circle(r):
    Area=r*r*math.pi
    print(Area)
def trapezoid(a,b,hight):
    Area=(((a*b)*hight)/2)
    print(Area)
form=str(input('Pick a cirlce or trapezoid: '))
if form=='circle':
    r=int(input('r= '))
    circle(r)
elif form=='trapezoid':
    a=int(input('a= '))
    b=int(input('b= '))
    hight=int(input('hight= '))
    trapezoid(a,b,hight)
else:
    print('Enter a valid form')