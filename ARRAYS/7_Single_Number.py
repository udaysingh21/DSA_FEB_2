def singlenumber(arr):
    # O(n)/O(n)
    """approach-1"""
    # dicti={}
    #
    # for ele in arr:
    #     if ele not in dicti:
    #         dicti[ele]=1
    #     else:
    #         dicti[ele]+=1
    #
    # for key in dicti:
    #     if dicti[key]==1:
    #         # ans.append(key)
    #         return key
    #
    # return -1

    """Optimised approach"""
    # O(n)/O(1)
    ans = 0
    # ele^ele=0
    # ele^0=ele
    # duplicate elements gets cancelled out and single element stores in ans
    for ele in arr:
        ans = ans ^ ele

    return ans

nums = [4,1,2,1,2]
print(singlenumber(nums))