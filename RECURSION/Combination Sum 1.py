def combinationsum1(i,arr,tar,temp,ans):
    if tar==0:
        ans.append(temp.copy())
        return

    if i>=len(arr): return

    # not pick
    combinationsum1(i+1,arr,tar,temp,ans)

    # pick
    if arr[i]<=tar:
        temp.append(arr[i])
        combinationsum1(i,arr,tar-arr[i],temp,ans)
        temp.pop()


arr=[2,3,5]
target=8
temp=[]
ans =[]

combinationsum1(0,arr,target,temp,ans)
print(ans)