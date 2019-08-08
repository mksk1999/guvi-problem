n=int(input())
s=str(n)
a=0
if(len(s)==1):
    a=int(s[0])**2
else:
    for i in range(len(s)):
        if(i!=(len(s)-1)):
           a+=(int(s[i])**int(s[i+1]))
        else:
           a+=(int(s[i])**int(s[0]))
print(a)
