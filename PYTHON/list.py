# List is equivalent to Array
# List - heterogeneous , multiple items store in single variable [1,a,True]
# mutable

a=list()
# print(type(a))
#
b=[]

thislist=['apple','banana','orange','apple','orange']
# print(type(thislist))
#
# print(thislist[2])

"""Ordered"""
# list have defined order and it will not change

"""Changeable"""
# Add/Update
thislist[1]='mango'
print(thislist)

# insert(idx,value)
thislist.insert(2,'kiwi')
print(thislist)

# append()
thislist.append('watermelon')
print(thislist)

# Remove/Delete
thislist.remove('orange') # deletes first occurence of element only
print(thislist)

# Pop()
thislist.pop(1) # deletes element at particular index
print(thislist)

thislist.pop() # removes last element by default
print(thislist)

thislist.clear() # removes all the elements only
print(thislist)

del thislist # deletes entire list
# print(thislist)

"""Duplicates allowed"""
# thislist=['apple','banana','orange','apple','orange']
# print(thislist)
#
# print(len(thislist))


