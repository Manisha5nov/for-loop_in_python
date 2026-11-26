n=int(input("enter a umber"))
sum=0
for i in range(1,n+1):
    b=n%10
    sum=sum+b
    n=n//10  
print(sum)
