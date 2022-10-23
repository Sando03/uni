x = str(input('enter: '))

for i in range(0,5):
    x=x.replace(str(i),'0')
for i in range(5,10):
    x=x.replace(str(i),'1')
print(x)