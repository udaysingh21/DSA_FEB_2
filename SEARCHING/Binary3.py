def first_binary(arr,n,x):
    l=0
    h=n-1

    while l<=h:
        m=(l+h)//2
        if arr[m]==x:
            '''when we got our key'''
            if m==0: return m
            elif arr[m-1]<arr[m]: return m
            else:
                h=m-1
        elif arr[m]<x:
            l=m+1
        else:
            h=m-1

    return -1

def last_binary(arr,n,x):
    l = 0
    h = n - 1

    while l <= h:
        m = (l + h) // 2
        if arr[m] == x:
            '''when we got our key'''
            if m == n-1:
                return m
            elif arr[m + 1] > arr[m]:
                return m
            else:
                l = m + 1
        elif arr[m] < x:
            l = m + 1
        else:
            h = m - 1

    return -1


array=[1,1,2,2,2,2,2,2,2,2,3]
first=first_binary(array,11,25)
last=last_binary(array,11,2)
if first==-1 or last==-1: print(0)
else: print(last-first+1)