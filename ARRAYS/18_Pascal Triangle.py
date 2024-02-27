def pascaltriangle(n):
    pascal = [[1] * (i + 1) for i in range(n)]

    for i in range(numRows):
        for j in range(1, i):
            # By observation
            pascal[i][j] = pascal[i - 1][j - 1] + pascal[i - 1][j]

    return pascal

print(pascaltriangle(5))