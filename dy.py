import random
x= random.randint(1000, 9999)
sum=0

while(x!=0):
    sum+=(x%10)
    x= x//10

print(sum)
if sum%2==0:
    print('True')
else:
    print('False')
    
