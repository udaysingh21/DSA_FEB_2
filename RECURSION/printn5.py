def fun(i,n):
    if i>n: return

    print(i)
    fun(i+1,n)

fun(1,5)