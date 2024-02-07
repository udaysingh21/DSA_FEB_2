def singlenumber(arr):
    # O(n)/O(n)
    dicti={}

    for ele in arr:
        if ele not in dicti:
            dicti[ele]=1
        else:
            dicti[ele]+=1

    for key in dicti:
        if dicti[key]==1:
            # ans.append(key)
            return key

    return -1

nums = [4,1,2,1,2,4]
print(singlenumber(nums))