def duplicate(arr):

    arr.sort() # O(nlogn)
    n=len(arr)
    for i in range(n-1): # O(n)
        if arr[i]==arr[i+1]:
            return True

    return False


def duplicate1(arr):
    # O(n)/O(n)
    dicti = {}
    # {arr[i]:frequency}

    for ele in arr:
        if ele not in dicti:
            dicti[ele] = 1  # assign element 1 as it appears first time
            # dict[key]=value
        else:
            # dicti[ele]+=1
            # if dicti[ele]==2:
            #     return True
            return True



arr=[1,2,3,0,4,1]
print(duplicate1(arr))