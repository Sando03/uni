import random
n=int(input('n= '))
list1=[]
for i in range(n):
    list1.append(random.randint(0,100))
list1.sort()
print(list1)
print(list1[n-1])