def subset(arr,i,temp,ans):
    if i>=len(arr): # when index exceeds or equals the length of array
        print(temp)
        ans.append(sum(temp))
        return

    # not pick
    subset(arr,i+1,temp,ans)

    # pick
    temp.append(arr[i])
    subset(arr,i+1,temp,ans)
    temp.pop()


if __name__=="__main__":
    arr=[5,2,1]
    temp=[] # it will store all possible combination (subset)
    ans=[] # it will store sum of subsets
    subset(arr,0,temp,ans)
    print(ans)