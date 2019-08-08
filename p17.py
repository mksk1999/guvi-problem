n=int(input())
s=str(n)
a=0
for i in range(len(s)):
    a+=(int(s[i])**len(s))
print(a)
