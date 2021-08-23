s=input('Enter a word')
ss=input("Enter another word")

def reverse(s):
    s,a=s,''
    k=len(s)-1
    for i in range(len(s)):
        a+=s[k]
        k-=1
    return a

def eqcheck(s,ss):
    s,ss=s,ss
    if s==ss:
        return 'Equal'
    else:
        return 'Not Equal'

def palindrome(s):
    if s==reverse(s):
        return 'Palindrome'
    else:
        return 'Not Palindrome'



print(len(s),len(ss))
print(reverse(s),reverse(ss))
print(eqcheck(s,ss))
print(palindrome(s),'  ',palindrome(ss))
