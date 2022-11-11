def f(list1=[]):
    even=[]
    odd=[]
    for i in range(len(list1)):
        if list1[i]%2==0:
            odd.append(list1[i])
        else:
            even.append(list1[i])
    print(even)
    print(odd)

f([1,2,3,4,5,6])