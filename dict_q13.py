my_dict = {
    'a':50, 
    'b':58,
    'c': 56,
    'd':40,
    'e':100, 
    'f':20
    }

a=[]
for i in my_dict.values():
    a.append(i)
p=sorted(a)
y=1
u=[]
while y<=3:
    u.append(p[-y])
    y+=1    
print(u)            