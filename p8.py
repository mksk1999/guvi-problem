n=int(input())
b=[]
s=0
for i in range(n):
  l=list(map(int,input().split()))
  b.append(l)
for i in range(len(b)):
  s+=b[i][i]
print(s)
