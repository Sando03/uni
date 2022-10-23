import random
n=random.randint(1000,9999)
list=[]
print(n)
while n!=0:
    digit=n%10
    list.append(digit)
    n//=10
print (list)
