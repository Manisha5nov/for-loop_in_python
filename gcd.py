a=int(input("enter a number :"))
b=int(input("enter a number :"))
while b!=0:
    a,b=b,a%b
print("gdc is",a)
