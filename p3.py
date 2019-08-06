s=input()
c=0
l=[]
for i in s:
  c=s.count(i)
  if(c==1):
    l.append(i)
for i in l:
  print(i,end="")
    
