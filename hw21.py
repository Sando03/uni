def v(text):
    dic={}
    up=0
    low=0
    for i in range(len(text)):
        if text[i].isupper():
            up=up+1
        else:
            low=low+1
    for i in text:
        if i not in dic:
            dic[i]=1
        else:
            dic[i]+=1
           
    print(dic)
    print(up)
    print(low)

v('DSdd')
