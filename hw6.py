list1=[1,2,3,4,5]
list2=[]
for i in range(len(list1)-1):
    sum= list1[i]+list1[i+1]
    list2.append(list1[i+0])
    list2.append(sum)
    sum=0
list2.append(list1[4])
print (list2)