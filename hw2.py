text = input("Paste your text here: ")
sum=0
word_list=text.split()
for i in word_list:
    if len(i)==5:
        sum=sum +1
print (sum)
