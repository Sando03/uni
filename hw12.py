def ispalindrome(text):
    return text==text[::-1]

text='malayalam'
ans=ispalindrome(text)

if ans==True:
    print('Yes')
else:
    print('No')