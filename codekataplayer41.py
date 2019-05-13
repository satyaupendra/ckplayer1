n,k=list(map(int,input().split()))
if(n>=0 and k>=0):
    for i in range(n):
        if(pow(k,i)==n):
            t=1
            break
        else:
            t=0
    if(t==1):
        print("yes")
    else:
        print("no")
else:
    print('invalid input')