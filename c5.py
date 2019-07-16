from itertools import combinations
n,k=map(int,input().split())
m=len(str(n))
a=list(combinations(str(n),m-k))
a.sort()
print(*a[0],sep='')


