def rbw(arr):
    cz,co,ct=0,0,0

    for i in range(len(arr)):
        if arr[i]==0:
            cz+=1
        elif arr[i]==1:
            co+=1
        else:
            ct+=1

    i=0
    while cz!=0:
        arr[i]=0
        cz-=1
        i+=1

    while co!=0:
        arr[i]=1
        co-=1
        i+=1

    while ct!=0:
        arr[i]=2
        ct-=1
        i+=1


array=[2,0,0,1,0,0,2]
rbw(array)
print(array)

