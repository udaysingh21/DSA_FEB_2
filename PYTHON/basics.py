# INPUT/OUTPUT

# name=input("Please enter your name: ")
# print(name)

"""By default input is always is in string format"""

# age=int(input("Please enter your age: "))
# print(age)
# print(type(age))

# print(type(10.5))

# print(type(True))

"""In python, we don't have to declare datatype"""

#  1 2 3 4 5
# ARRAY = 1 2 3 4 5
# array = list(map(int,input().split()))
# print(array)
# print(type(array[0]))

# input() - '1 2 3 4 5'
# input.split() - '1' '2' '3' '4' '5'
# map(int,input.split()) - 1 2 3 4 5
# list(map(int,input.split())) - [1 2 3 4 5]

"""SPLIT I/O"""

# question - arary= [1 2 3 4 5]
array=input() # '1 2 3 4 5'
print(array)
print(type(array))

arr=array.split() # removes space and convert into individual elements
print(arr)

object=map(float,arr) # we get a map object and we convert it to list

print(list(object))
