def setmatrix0(mat,m,n):
    row=set()
    col=set()

    for r in range(m):
        for c in range(n):
            if mat[r][c]==0:
                row.add(r)
                col.add(c)

    # setting rows to 0
    for r in row:
        for j in range(n):
            mat[r][j]=0

    # setting columns to 0
    for c in col:
        for i in range(n):
            mat[i][c]=0

matrix=[[0,0,1],[0,1,1],[1,1,1]]
setmatrix0(matrix,3,3)
print(matrix)