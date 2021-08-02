str=input('Enter any sentence')
k,c,i=len(str),0,0


while i<k-1:
    if str[i]=='a' and str[i+1]=='r' and str[i+2]=='e':
        c+=1
    else:
        pass
    i+=1

print(c)


