def f(list,n):
    for i in range(len(list)):
        if list[i] > n:
            list[i]=0
    print(list)

f([1,2,3,4,5,6,7],3)