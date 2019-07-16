n,k=map(int,input().split())
a=list(map(int,input().split()))
a.sort()
l=[]
for i in a:
    l.append(k-i)
l.sort()
l.remove(0)
for i in range(3):
    print(k-l[i],end=" ")
             
    
        

