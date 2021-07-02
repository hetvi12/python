n=int (input("Enter Range for Fibonacci Series:"))

a,b=0,1
while b<n:
    print (b,end=" ")
    a,b=b,a+b
    
