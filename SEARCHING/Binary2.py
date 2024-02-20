def transitionpoint(arr,n):
    l=0
    h=n-1

    while l<=h:
        m=(l+h)//2
        if arr[m]==1:
            # check if its first one or not
            if m==0: return m
            elif m!=0 and arr[m-1]<arr[m]:
                return m
            else:
                h=m-1
        elif arr[m]<1:
            l=m+1

    return -1

array=[1,1,1,1,1,1,1]
array1=[0,0,0,0,0,0,0]
print(transitionpoint(array1,7))