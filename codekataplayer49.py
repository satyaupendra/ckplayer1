n=int(input())
if(n in range(-(2**15),(2**15))):
    print("INT")
elif(n in range(-(2**31),(2**31))):
    print("LONG")