def search(nums: List[int], target: int) -> int:
    # modified binary search - O(logn)
    n = len(nums)
    l, h = 0, n - 1

    while l <= h:
        mid = (l + h) // 2
        if nums[mid] == target: return mid
        if nums[l] <= nums[mid]:  # left part sorted (so we can apply binary search)
            if nums[l] <= target < nums[mid]:  # whether target is in left part or not
                h = mid - 1
            else:
                l = mid + 1
        else:  # right part sorted (so we can apply binary search)
            if nums[mid] < target <= nums[h]:
                l = mid + 1
            else:
                h = mid - 1
    return -1

print(search([4,5,6,7,0,1,2],0))