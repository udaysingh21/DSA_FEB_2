# Tuple
# Immutable , Allow Duplicates, unchangeable

a=tuple()
# print(type(a))

b=()
# print(type(b))

thistuple=('apple','banana','cherry')
print(type(thistuple))

# Access
print(thistuple)
print(thistuple[2])

"""Ordered"""
# items have defined order and it will not change

"""Duplicates allowe"""
thistuple=('apple','banana','cherry','cherry')
print(thistuple)

# age='18'
# print(type(int(age)))
# print(int(age))

# Inorder to modify tuple firsr convert it into list
thistuple=list(thistuple)
print(type(thistuple))
# operations
thistuple=tuple(thistuple)
