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
            # if we found reqd then return their indexes
            # return [reqd,arr[i]]
            return [dicti[reqd],i]
        else:
            # if reqd not in dicti store arr[i] with index as its value for future use
            dicti[arr[i]]=i # we are storing index i

    return [-1,-1]


print(twosum1([8,29,3,9,7,2],5))