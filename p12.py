s1,s2=map(str,input().split())
b=len(s1)
c=len(s2)
a=max(b,c)
d=[]
j=1
for i in range(0,a):
    if(b>c):
        d.append(s1[i])
        if(i<c):
            d.append(s2[i])
        else:
            d.append(j)
            j+=1
    elif(b<c):
        if(i<b):
            d.append(s1[i])
        else:
            d.append(j)
            j+=1
        d.append(s2[i])
    else:
        d.append(s1[i])
        d.append(s2[j])
for i in d:
    print(i,end="")
            
      
