#eg.1
# city_population = {
#     "NewYorkCity":8550405,
#     "LosAngeles":3971883, 
#     "Toronto":2731571, 
#     "Chicago":2720546, 
#     "Houston":2296224, 
#     "Montreal":1704694, 
#     "Calgary":1239220, 
#     "Vancouver":631486, 
#     "Boston":667137
# }
# print(city_population["NewYorkCity"])
# print(city_population)
# print(type(city_population))

#eg.2
# Dict1={
#        'ball' : 'green',
#        'Ball': 'red'
#     }
# print(Dict1['ball'])
# print(Dict1['Ball'])
# print(Dict1['bat'])

#eg.3
# student=dict(name= "Ravina",age= 20)
# print(student)

#eg.4
# my_dict = {
#     1: 'apple', 
#     2: 'ball'
#     }
# print(my_dict)

#eg.5
# dictionary with mixed keys:-

# my_dict = {
#     'name': 'John',
#      1: [2, 4, 3]
#     }
# print(my_dict)

#eg.6 
# nested dictionary
# Dic= {
#  1: 'NAVGURUKUL',
#  2: 'IN',  
#  3:{
#      'A' : 'WELCOME',
#      'B' : 'To', 
#      'C' : 'DHARAMSALA'
#      }
# }
# print(Dic)
# print(Dic[3])
# print(Dic[3]['A'])

#eg.7
#accesing eliment from  dictionery
# person={
#     'name':'jack',
#     'age':20,
#     'gender':'male',
#     4:'organisation'}
# result = person['age'] 
# x = person.get("gender")#get is used to fatch the data(or get a value from dictionery)same as square breaket
# print(person[4])
# print(x)
# print(result)

#eg.8get() :-.get
#We can also make use of the get() function to access dictionary values
# person={
#     'name':'jack',
#     'age':20,
#     'gender':'male',
#     4:{
#         'organisation':'navgurukul','place':'dharamsala'
#         }
#     }
# print(person['gender'])
# print(person[4])
# #We can also make use of the get() function to access dictionary values
# x = person.get("gender")
# print(x)
# result = person[4]['place']
# print(result)

