def reverse1(arr):
    i,j=0,len(arr)-1

    while i<=j:
        arr[i],arr[j]=arr[j],arr[i]
        i+=1
        j-=1

def insertbottom(stack,val):
    if not stack:
        stack.append(val)
        return

    val1=stack.pop()
    insertbottom(stack,val)
    stack.append(val1)

def reverse2(stack):
    if not stack:
        return

    val=stack.pop()
    reverse2(stack)
    insertbottom(stack,val)

arr=[1,2,3,4,5]
reverse2(arr)
print(arr)