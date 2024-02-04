# Dictionary - key value pair

d=dict()
d2={}

# print(type(d))
# print(type(d2))


# Key-immutable always
# Value-mutable/immutable
dicti1={
    'name':'uday vikram singh',
    'age':18,
    'course':'Btech.',
    'marks':[10,8,9],
}

# print(dicti1)

# array of dictionaries
students=[
    {
    'name':'uday vikram singh',
    'age':18,
    'course':'Btech.',
    'marks':[10,8,9],
    },

    {
    'name':'adarsh',
    'age':18,
    'course':'Btech.',
    'marks':[10,8,9],
    }

]

for i in range(len(students)): # for accesing students
    student=students[i]
    for key in student: # for accesing particular student's details
        print(key,student[key])


# print(students)
first=students[0]
# print(first)

# Access in Dictionary

# dict_name[key]=value
# print(first['name'])
# print(first['age'])
# print(first['course'])
# print(first['marks'])

dicti={
    'name':'uday vikram singh',
    'age':18,
    'course':'Btech.',
    'marks':[10,8,9],
}

for key in dicti:
    print(key, dicti[key])


# Ordered or Unordered ?

# Dictionaries share ordered


# Changeable
# Dictionaries are changeable i.e which means add or removed items after dictionary has been created


dicti['name']='Adarsh Singh'
print(dicti)

dicti['marks']=(10,20,30,40)
print(dicti)
# print(dicti['marks'].append(50))
print(dicti['marks'])

dicti['marks']=100
print(dicti)



# UPDATE
print(dicti)
# dicti['age']=20
# dicti['gender']='male'

dicti.update( {'age':20} )
dicti.update( {'gender':'male'} )
print(dicti)


grocery= {'rice': 20, 'dal': 10}
print(grocery)

grocery['rice']=5 # directly
print(grocery)

grocery['sugar']=3 # directly
print(grocery)


grocery.update( {'oil':10} )
print(grocery)





# REMOVE VALUE
grocery.pop('oil') # removes specified key
print(grocery)

grocery.popitem() # removes last inserted item
print(grocery)

del grocery['rice']
print(grocery)

grocery['rice']=10
grocery['oil']=100

print(grocery)

grocery.clear()
print(grocery)