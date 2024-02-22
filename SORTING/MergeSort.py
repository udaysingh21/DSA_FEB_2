def mergesort(arr,l,r):
    if l<r:
        m=(l+r)//2

        mergesort(arr,l,m)
        mergesort(arr,m+1,r)
        merging(arr,l,m,r)


def merging(arr,l,m,r):
    i=l
    j=m+1
    temp=[0]*(r-l+1)
    k=0

    while i<=m and j<=r:
        if arr[i]<=arr[j]:
            temp[k]=arr[i]
            k+=1
            i+=1
        else:
            temp[k]=arr[j]
            k+=1
            j+=1

    while i<=m:
        temp[k]=arr[i]
        k+=1
        i+=1

    while j<=r:
        temp[k]=arr[j]
        k+=1
        j+=1

    i=l
    for val in temp:
        arr[i]=val
        i+=1




array=[8,2,-1,4,0,-3]
mergesort(array,0,len(array)-1)
print(array)
