n=int(input())
t=0
for i in range(2,n//2):
    if(n%i==0):
        t=1
        break
if(t==1):
    print("yes")
else:
    print("no")