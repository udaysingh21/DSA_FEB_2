def reverse(arr):
    # Brute Force
    ans=[]

    # for (i=n-1;i>=0;i--)
    #   print()

    n=len(arr)
    for i in range(n-1,-1,-1):
        print(i,arr[i])
        ans.append(arr[i])

    return ans


def reverse2(arr):
    """Two-pointer approach"""
    n=len(arr)
    # i,j index
    i=0
    j=n-1

    while i<=j:
        # if we swap after i<=j, we will get oiginal array
        arr[i],arr[j]=arr[j],arr[i]
        i+=1
        j-=1

    return arr

def reverse3(arr,m):
    """Two-pointer approach"""
    n=len(arr)
    # i,j index
    i=m+1
    j=n-1

    while i<=j:
        # if we swap after i<=j, we will get oiginal array
        arr[i],arr[j]=arr[j],arr[i]
        i+=1
        j-=1

    return arr

array=[1,2,3,4,5,6,7,8]
print(reverse3(array,2))