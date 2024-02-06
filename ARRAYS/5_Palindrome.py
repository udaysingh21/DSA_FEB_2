def palindrome(arr):

    i=0
    j=len(arr)-1 # j=n-1

    while i<=j:
        if arr[i]!=arr[j]:
            return False
        else:
            i+=1
            j-=1

    return True


def PalinArray(arr, n):
    # O(n2)/O(1)
    for num in arr:
        num = str(num)  # converted to use 2-pointer approach
        i = 0
        j = len(num) - 1

        while i <= j:
            if num[i] != num[j]:
                return False
            else:
                i += 1
                j -= 1

    return True

print(palindrome('madam'))
print(palindrome('peacdaep'))

print(PalinArray([111,222,333,444,555],5))
print(PalinArray([111,222,333,444,567],5))