i=0
dic={}
while i<10:
    name=input("enter name here:")
    marks=int(input("enter marks"))
    dic[name]=marks
    i+=1
print(dict(dic))
    