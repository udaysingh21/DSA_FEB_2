def swapkth(arr,k):
    arr[k-1],arr[-1*k]=arr[-1*k],arr[k-1]

array=[1,2,3,4,5,6,7,8]
swapkth(array,3)
print(array)