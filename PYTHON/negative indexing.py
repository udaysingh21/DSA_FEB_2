array=[1,2,3,4,5]
#      0,1,2,3,4
#      -5,-4,-3,-2,-1
#      i-length = negative indexing

a=array[0]
b=array[-5]

print(a,b)

print("Value at index {i} is {val}".format(i=0,val=a))

txt1="My name is {fname}, I'm {age} year old".format(fname="Uday",age=20)
print(txt1)

fname='UDAY'
age=18

print(f"my name is {fname} and my age is {age}")

for pos_i in range(len(array)):
    print("Positive index",pos_i,'holds value',array[pos_i])

    neg_idx = pos_i-len(array) # negative index
    print("Negative index",neg_idx,'holds value',array[neg_idx])


arr=['uday',1,True,234,12]

# range(start,end,update)
"""Reverse Loop"""
# range(length-1,-1,-1)

# for i in range(len(arr)):
#     print(arr[i],end=' , ')

# for i in range(len(arr)-1,-1,-1):
    # print(i,arr[i])

"""Print directly without index"""
for element in arr:
    print(element)

