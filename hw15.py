def f(text):
    sumup=0
    sumlow=0
    for i in range(len(text)):
        if text[i].isupper():
            sumup=sumup+1
        else:
            sumlow=sumlow+1
    print(sumup)
    print(sumlow)
f('FAFsad')