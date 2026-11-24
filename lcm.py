import math
a=int(input("enter a number :"))
b=int(input("enter a number :"))
lcm=(a*b)//math.gcd(a,b)
print("lca is :",lcm)
