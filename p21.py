n=int(input())
if(n==2 or n==1):
    print("0")
for i in range(2,n):
    c=1
    for j in range(2,n):
        if(i%j==0):
            c+=1
    if(c==2):
        print(i,end=" ")

    
