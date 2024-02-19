def binarysearch(arr, n, key):
    # O(logn)/O(1)
    l = 0
    h = n - 1

    while l <= h:
        m = (l + h) // 2
        if arr[m] < key:
            l = m + 1
        elif arr[m] > key:
            h = m - 1
        else:
            return m

    return -1

print(binarysearch([12,24,35,46],4,24))