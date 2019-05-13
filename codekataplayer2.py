n=int(input())
if(n>=0):
   if(n==1 or n==0):
	   factorial=1
   else:
	   factorial=1
	   for i in range(1,n+1):
		   factorial=factorial*i
   print(factorial)
else:
    print("invalid")
