#eg.2
#Adding Elements to a Dictionary:-i
# n a python dictionary we can add only one key value pair at a time. 
# To add to a dictionary we mention the key inside square brackets "[ ]"
#  and use the equal to "=" operator`` to assign a value
# dic= {
#     'Name': 'RAM', 
#     'Age': 17,
#     }   
# dic['ORGANIZATION'] = "NAV GURUKUL"
# dic['place'] = 'dharamsala'
# dic['state']='himachal'
# print(dic)

# eg.2
# dic= {
#     'Name': 'RAM',
#     'Age': 17,
#      }
# dic['student']={
#         'id':22, 
#         'place':'dharamsala'
#     }
# print(dic)


#Key Exists or not
# We use the in keyword to check whether a given key exists
#  or not in a dictionary
# car ={
#     "brand":  "ford",
#     "model":  "mustang",
#     "year":  1964
# }
# if "model" in car:
#     print("Yes, 'model' is one of the keys in the car dictionary.")

# else:
#     print("No, 'model' key dictionary mai nahi hai.")

#################################################
#UPDATE DICTIONARY
# Updating Dictionary :-
# To update dictionary ,we can make an entry in it or we can add a key-value pair 
# or we can change the value of an existing key. As given in the example explained:-
# person= {'1': 'RAM', '2': 17,}
# person[3] = 'male'
# print(person)

#eg.2 updation
# details={
#     'Name': 'RAM',
#      'Age': 17, 
#      'student': {
#       'id': 22,
#       'place': 'dharamsala'
#       }
#      } 
# details['student']['id']=35
# print(details)

#############################
#Copy of Dictionary :-
# We can copy a dictionary in two ways,first method is using copy() and 
# second method by using built-in function dict().
# classes ={
#     "room1":  "6th",
#     "room2":  "7th",
#     "room3":  "8th"
#         }
# mydict=classes.copy()#to copy a dictionery
# print(mydict)

#########################################################
#Removing Elements from a Dictionary:-We can remove dictionary elements by many methods. Like given below.
# pop() :Using the pop( ) 
# method we can remove a specified element from the dictionary.
CAR_DETAILS={
    "brand": "Ford",
    "model": "jason",
    "year": 1964
}
CAR_DETAILS.pop("model")
# CAR_DETAILS.pop("year")
print(CAR_DETAILS)

# popitem():-
# The popitem() method removes the last inserted item:
# person={
#     'name':'jack',
#     'id':22,
#     'place':'dharamsala'
# }
# person.popitem()
# print(person)

#del :-
#Using the del keyword we can remove a specified element from the
#dictionary.
# person={
#     'name':'jack',
#     'id':22,
#     'place':'dharamsala'
# }
# del person['place']
# print(person)

