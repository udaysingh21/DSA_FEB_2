def intersection(arr1,arr2):
    p=set(arr1)
    q=set(arr2)

    return p.intersection(q)

print(intersection([1,2,2,1],[2,3,4,5]))
