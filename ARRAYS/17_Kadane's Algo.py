def maxsumsubarray(arr):
    # max_sum=float('-inf')
    #
    # n=len(arr)
    # for i in range(n):
    #     for j in range(i+1,n+1):
    #         sub=arr[i:j] # [-2,1,1]
    #         # max_sum=max(max_sum,sum(sub))
    #         if sum(sub)>max_sum:
    #             max_sum=sum(sub)
    #
    # return max_sum

    curr_sum = 0
    max_sum = float('-inf')

    for i in range(len(nums)):
        curr_sum += nums[i]
        max_sum = max(max_sum, curr_sum)
        if curr_sum < 0:
            curr_sum = 0

    return max_sum



array=[-2]
print(maxsumsubarray(array))