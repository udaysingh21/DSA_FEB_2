def sumn(total,i,n):
    if i>n:
        return total[0]

    total[0]+=i
    return sumn(total,i+1,n)



total=[0]
print(sumn(total,1,5))
print(total[0])


def fun(n):
    # jab first natural number ka sum mnga ja rha hai to 1 return kr do
    if n==1: return 1
    else:
        return n+fun(n-1)

print(fun(7))
