a={}
user=input("take any name :")
for i in range(len(user)):
    key= i 
    value=user[i]
    a.update({key:value})
print(a)