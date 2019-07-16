n=int(input())
l=list(map(int,input().split()))
a=[]
for i in range(n):
    b=l[i:]
    a.append(sum(b))
print(max(a))


             
    
        
