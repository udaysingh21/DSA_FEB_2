# For , While Loop
array=[1,2,3,4,5]

# for(i=0;i<array.length;i+=2){
#   print(array[i])
#}

"""Range function"""
# By default, starts from 0 to n-1
# range(5)=0 1 2 3 4
# range(8)= 0 1 2 3 4 5 6 7
# range(3,8)=3 4 5 6 7
# range(2,6)=2 3 4 5
# range(2,10,2)=2  4  6  8
# range(4,14,3)=4

# for i in range(4,14,3):
#     print(i)


# n=len(array) # 0 1 ... n-1
# for i in range(n):
#     print(array[i])
#
# name="Uday Vikram Singh"
# print(name)
# # length=n  indexin - 0...n-1
# for i in range(2,len(name),2):
#     print(name[i])
#

"""WHILE LOOP"""
array1=[1,'a',2,234.45,True,"Uday",23456567.453627891234857] # in list, we can store HETEROGENEOUS Value

# n=len(array1)

i=0
# while i!=len(array1):
#     print(i,array1[i])
#     i+=1

# CONTINUE/BREAK

for i in range(10):
    print(i)
    if i==4:
        break

for i in range(10):
    if i%2==1:
        continue
    else:
        print(i)