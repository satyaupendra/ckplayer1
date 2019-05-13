p,a=list(map(int,input().split()))
n=p//2
t=0
for i in range(n):
    for j in range(n):
        if(i*j==a):
           t=1
           break
if(t==1):
    print('yes')
else:
    print("no")