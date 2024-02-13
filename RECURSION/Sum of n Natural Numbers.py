def sumn(total,i,n):
    if i>n:
        return total[0]

    total[0]+=i
    return sumn(total,i+1,n)



total=[0]
print(sumn(total,1,5))
print(total[0])