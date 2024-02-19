def search(arr, N, X):
    # Your code here
    for i in range(N):
        if arr[i] == X:
            return i

    return -1

ans=search([1,2,3],5,2)
print(ans)