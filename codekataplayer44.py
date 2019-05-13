n,l=map(str,input().split())
l=int(l)
t=len(n)-l
print(n[t:]+n[:t])
