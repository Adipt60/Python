str=input('Enter any word')
k=len(str)
strr=[]
strrr=[]
for i in range(len(str)):
    strr.append(str[k-1])
    k-=1

for i in range(len(str)):
    strrr.append(str[i])


if strrr==strr:
    print("Palindrome")
else:
    print("Not Palindrome")