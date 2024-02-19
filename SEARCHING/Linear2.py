def search(arr, N, X):
    # Your code here
    for i in range(N):
        if arr[i] == X:
            return i

    return -1

print(search([1,2,2,33,4],5,2))