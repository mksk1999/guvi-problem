s,a=map(str,input().split())
c=0
for i in range(len(a)):
  if(a[i] in s):
    c+=1
if(c==len(a)):
  print("yes")
else:
  print("no")
