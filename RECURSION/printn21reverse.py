def n21reverse(n):
    if n==0: return

    n21reverse(n-1)
    # code...
    print(n)

n21reverse(7)