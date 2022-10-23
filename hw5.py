list1=[1,3,350,450,20]
list2=[]
sum=0
for i in range(len(list1)-1):
    sum= list1[i]+list1[i+1]
    list2.append(sum)
print (list1)
print (list2)
