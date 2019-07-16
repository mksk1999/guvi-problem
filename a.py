n=int(input())
a=list(map(int,input().split()))
l=len(a)
for i in range(l):
    for j in range(l):
        for k in range(l):
                if(a[i]!=a[j]):
                    if((a[i]+a[j]==a[k]) and (i<j<k)):
                        print(a[i],a[j],a[k])
                        
                        

