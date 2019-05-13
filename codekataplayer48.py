n=int(input())
l=[]
for i in range(1,n+1):
    if(n%i==0):
        if(i% 2!=0 or i==2):
            l.append(i)
print(" ".join(map(str,l)))
            