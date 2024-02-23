def majroity(arr,n):
    dicit={}

    for val in arr:
        if val not in dicit:
            dicit[val]=1
        else:
            dicit[val]+=1
            if dicit[val]>n//2:
                return val




array=[2,2,1,1,1,2,2,1,1,1]
print(majroity(array,10))