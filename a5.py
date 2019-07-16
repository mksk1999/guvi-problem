n=int(input())
a=list(map(int,input().split()))
a.sort()
b=a[::-1]
print("->".join(map(str,b)))
