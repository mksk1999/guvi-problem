n=int(input())
s=str(n)
a=0
for i in range(len(s)):
    for j in range(i+1):
        a+=int(s[j])
print(a)
