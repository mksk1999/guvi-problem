import math
n=int(input())
b=[]
for i in range(2,n):
    c=1
    for j in range(2,n):
        if(i%j==0):
            c+=1
    if(c==2):
        b.append(i)
s=0
for i in range(len(b)):
    for j in range(1,len(b)):
        if(b[i]+b[j]==n):
            s+=1
print(math.ceil(s/2))
