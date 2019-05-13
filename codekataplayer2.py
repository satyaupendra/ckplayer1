n=int(input())
if(n>=0):
   if(n==1 or n==0):
	   t=1
   else:
	   t=1
	   for i in range(1,n+1):
		   t=t*i
   print(t)
else:
    print("invalid")
