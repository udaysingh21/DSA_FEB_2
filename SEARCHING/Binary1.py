def findfloor(arr,n,x):
    l=0
    h=n-1

    ans=-1
    while l<=h:
        m=(l+h)//2
        if arr[m]<=x:
            ans=m
            l=m+1
        else:
            h=m-1

    return ans



array=[1,2,8,9,11,12,15]
n=7
x=0
print(findfloor(array,n,x))