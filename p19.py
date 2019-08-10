import itertools
s=input()
l=list(itertools.permutations(s))
c=0
for i in range(len(l)):
    b=''
    for j in range(len(l[i])):
        b+=l[i][j]
    if(b!=s):
        c=1
if(len(s)==1 or c==1):
    print("yes")
else:
    print("no")
