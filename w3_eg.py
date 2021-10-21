# #Add a new item to the original dictionary
# car = {
# "brand": "Ford",
# "model": "Mustang",
# "year": 1964
# }

# x = car.keys()

# print(x) #before the change

# car["color"] = "white"

# print(x) #after the change




# a=0
# while a<10:
#     # print(a)
#     a+=1
#     print(a)
# # print(a)


a=[{"a":1,"data":"happy"},{"b":2,"data":"bday"},{"c":3,"data":"rash"}]
for i in range(len(a)):
    if a[i]==2:
        del a[i]
        break
print(a)
