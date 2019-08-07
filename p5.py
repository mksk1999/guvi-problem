n=int(input())
a=0
for i in range(2,n+1):
  c=1
  for j in range(2,n+1):
    if(i%j==0):
      c+=1
  if(c==2):
    s=str(i)
    if(s=='3' or s[-1]=='3'):
      b=int(s)
      a+=b
print(a)
  
  
