number = int(input('number: '))
list1=[]
dic={}
for i in range(number):
    list1.append(i+1)
list1.reverse()
for i in range(1,number+1):
    dic[i]=list1[i-1]
print(dic)
print(list1)
