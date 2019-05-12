num=int(input())
if(num>=0):
   if(num==1 or num==0):
	   fact=1
   else:
	   fact=1
	   for i in range(1,num+1):
		   fact=fact*i
   print(fact)
else:
    print("invalid")
