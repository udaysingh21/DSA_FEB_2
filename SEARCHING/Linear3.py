def search(arr, n, k):
    # code here
    for i in range(n):
        if arr[i] == k:
            return i + 1

    return -1

print(search([1, 2, 2, 33, 4], 5, 2))