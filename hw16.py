def f(list1=[]):
    list2=[]
    for i in range(len(list1)):
        if list1[i] not in list2:
            list2.append(list1[i])
        else:
            continue
    return list2
print(f([1,1,24,3,4,4,5,421]))