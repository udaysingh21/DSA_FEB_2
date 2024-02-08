def twosum(arr,target):
    n=len(arr)
    # O(n2)/O(1)
    for i in range(n):
        for j in range(i+1,n):
            if arr[i]+arr[j]==target:
                return [i,j]

    return [-1,-1]

# dicti[key]=value

def twosum1(arr,target):

    dicti={}

    for i in range(len(arr)):
        reqd=target-arr[i]

        if reqd in dicti:
            return [dicti[reqd],i]
        else:
            dicti[arr[i]]=i

    return [-1,-1]


print(twosum1([8,29,3,9,7,2],5))