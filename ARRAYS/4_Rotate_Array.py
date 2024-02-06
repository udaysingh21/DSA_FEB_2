def rotate(nums: List[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    n = len(nums)
    k = k % n  # removes un-productive rotations.
    nums[:] = nums[n - k:] + nums[:n - k]