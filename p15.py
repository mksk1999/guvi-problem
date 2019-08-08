n=int(input())
l=list(map(str,input().split()))
b=[]
for i in l:
    s=i.lower()
    b.append(s)
b.sort()
for i in b:
    print(i)
