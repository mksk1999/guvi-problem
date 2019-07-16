n=int(input())
l=list(map(int,input().split()))
a=[]
c=1
for i in range(n):
    for j in range(i,n):
        c=c*l[j]
        a.append(c)
    c=1
print(max(a))


             
    
        
