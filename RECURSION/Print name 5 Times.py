def print5(name,n):
    if n==5: return

    print(name)
    print5(name,n+1)

print5('Uday Vikram Singh',0)