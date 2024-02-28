def product(array):
    """O(n2)/O(n)"""
    ans=[]
    n=len(array)

    prod=1
    for i in range(n):
        for j in range(n):
            if i!=j:
                prod=prod*array[j]
        ans.append(prod)
        prod=1

    return ans


def product1(arr):
    """O(n)/O(n)"""
    n=len(arr)
    left=[1]*n # [1,1,1,1,1]
    right=[1]*n # [1,1,1,1,1]
    ans=[1]*n # [1,1,1,1,1]

    # Updating Left array
    for i in range(1,n):
        left[i]=left[i-1]*arr[i-1]

    # Updating Right array
    for i in range(n-2,-1,-1):
        right[i]=right[i+1]*arr[i+1]

    for i in range(n):
        ans[i]=left[i]*right[i]

    return ans


array=[1,2,3,4,5]
print(product1(array))