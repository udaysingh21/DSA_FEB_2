def subset(arr,i,temp,ans):
    if i>=len(arr): # when index exceeds or equals the length of array
        ans.append(temp.copy())
        return

    # not pick
    subset(arr,i+1,temp,ans)

    # pick
    temp.append(arr[i])
    subset(arr,i+1,temp,ans)
    temp.pop()


arr=[2,3,5]
temp=[] # it will store all possible combination (subset)
ans=[] # it will store sum of subsets
subset(arr,0,temp,ans)
print(ans)