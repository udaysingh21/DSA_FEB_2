def threesum(arr,n):
    arr.sort()
    ans=set()

    for k in range(n):
        reqd=0-(arr[k])
        i=k+1
        j=n-1

        while i<j:
            if arr[i]+arr[j]==reqd:
                ans.add((arr[i],arr[j],arr[k]))
                i+=1
                j-=1
            elif arr[i]+arr[j]<reqd:
                i+=1
            else:
                j-=1

    return ans


array=[-1,0,1,2,-1,-4]
print(threesum(array,6))