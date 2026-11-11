s=input("enter a string :")
count=0
for i in s:
    if i.isalpha() and i not in 'aeiouAEIOU':
        count+=1
print(f"number of consonants in the string is : {count}")
