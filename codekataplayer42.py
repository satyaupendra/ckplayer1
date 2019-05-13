n=int(input())
l=list(map(int,input().split()))
k=l.copy()
l.sort()
if(k==l):
    print("yes")
else:
    print("no")