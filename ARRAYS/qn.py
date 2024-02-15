# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
# **Example
# :**
# makefile
# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.

"""O(n)/O(1)"""

def largestsum(arr):

    curr_sum=0
    maxi=float("-inf")

    for val in arr:
        curr_sum+=val
        maxi=max(maxi,curr_sum)

        if curr_sum<0:
            curr_sum=0

    return maxi

if __name__=="__main__":
    nums=[-2,-1,-3,-4,-1,-2,-1,-5,-4]
    ans=largestsum(nums)
    print(ans)