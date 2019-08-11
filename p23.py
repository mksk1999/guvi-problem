n=int(input())
my_dict=dict()
my_dict[1]=3
t=3
if(n==1):
    t=3
a=t
for i in range(2,n+1):
    t-=1
    my_dict[i]=t
    if(t==1):
        t=a*2+1
        a=t-1
print(my_dict[n])
