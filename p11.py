n=int(input())
b=[]
a=str(n)
for i in range(len(a)):
  b.append(int(a[i])**i)
print(sum(b))
