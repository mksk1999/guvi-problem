n=int(input())
l=list(map(int,input().split()))
a=l
b=[]
while(len(a)!=1):
    for i in range(len(a)):
        if(i%2!=0):
            b.append(a[i])
    a=b
    b=[]
print(l.index(a[0]))


             
    
        
