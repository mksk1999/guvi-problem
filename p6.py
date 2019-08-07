n=int(input())
l=list(map(int,input().split()))
c=[]
for i in l:
    c.append(l.count(i))
    s=max(c)
    a=c.index(s)
print(l[a])
    
  
