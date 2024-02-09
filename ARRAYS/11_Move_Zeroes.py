def move_zeroes(arr):
    # O(n)/O(n)
    ans=[]
    zeroes=0

    for i in range(len(arr)):
        if arr[i]!=0:
            ans.append(arr[i])
        else:
            zeroes+=1

    for i in range(zeroes):
        ans.append(0)

    return ans


def move_zeroes1(arr):

    z=0
    for i in range(len(arr)):
        if arr[i]!=0:
            # swap only when u get non-zero element
            # swap non-zero with zero element and increment z
            arr[i],arr[z]=arr[z],arr[i]
            z+=1

    return arr

array=[21,3,0,4,0,0,2,1,0]
print(move_zeroes(array))
print(move_zeroes1(array))