def duplicate(arr):

    arr.sort() # O(nlogn)
    n=len(arr)
    for i in range(n-1): # O(n)
        if arr[i]==arr[i+1]:
            return True

    return False


def duplicate1(arr):
    # O(n)/O(n)
    dicti={}
    # {arr[i]:frequency}
    for ele in arr:
        if ele not in dicti: # agr pehli baar aa rha to dict me daal do
            dicti[ele]=1
        else: # agr doosri baar aa rha to True return kr do
            # dicti[ele]+=1
            # if dicti[ele]==2:
            #     return True
            return True

    return False



arr=[1,2,3,0,4,1]
print(duplicate1(arr))