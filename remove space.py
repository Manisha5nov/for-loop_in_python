s=input("enter a string :") 
new_s=""
for i in s:
    if i!=" ":
        new_s+=i
print("String after removing spaces:", new_s)
   
s=input("enter a string :")
new_s=s.replace(" ","")
print("String after removing spaces:", new_s)
