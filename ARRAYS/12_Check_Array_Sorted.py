def checkarraysorted(arr):
    d=0
    n=len(arr)
    for i in range(1,len(arr)):
        if arr[i-1]>arr[i]:
            d+=1

    if arr[n-1]>arr[0]:
        d+=1

    if d<=1: return True
    else: return False

array=[2,1,3,4]
print(checkarraysorted(array))