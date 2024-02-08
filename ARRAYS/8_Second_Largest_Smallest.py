def secondlargestsmallest(arr):
    ans=[]
    n=len(arr)

    # jab maximum find krna ho to minimum assign kro
    fl,sl=0,0
    for i in range(n):
        if arr[i]>=fl:
            sl=fl
            fl=arr[i]
        else:
            if arr[i]>sl:
                sl=arr[i]

    ans.append(sl)

    # jab minimum nikalna ho to maximum assign kro
    fs,ss=max(arr),max(arr)
    for i in range(n):
        if arr[i]<=fs:
            ss=fs
            fs=arr[i]
        else:
            if arr[i]<ss:
                ss=arr[i]

    ans.append(ss)

    return ans

arr=[2,9,3,4,7]
print(secondlargestsmallest(arr))
