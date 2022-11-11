def f(list1=[]):
    n=list1[1]-list1[0]
    list2=[]
    for i in range(len(list1)-1):
        if list1[i+1]-list1[i]==n:
            list2.append(1)
        else:
            list2.append(0)
    if 0 in list2:
        print('not monotonous')
    else:
        print('monotonous')

f([2,4,6,8])