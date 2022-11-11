import random
def f():
    list1=[]
    list2=[]
    for i in range(15):
        list1.append(random.randint(0,9))
    for i in list1:
        if i not in list2:
            list2.append(i)
        else:
            continue
        list2.sort()
    print(list2)
f()