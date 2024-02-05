def valueEqualToIndex( arr, n):
    # O(n)/O(n)

    ans = []  # empty list

    for i in range(n):
        if arr[i] == i + 1:
            ans.append(arr[i])

    return ans

valueEqualToIndex([1,2,2,3,5],5)