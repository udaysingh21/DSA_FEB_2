class Node:
    def __init__(self,value):
        self.data=value
        self.next=None

n=Node(7)
print(n.data,n.next)

p=Node(8)
print(p.data,p.next)

q=Node(9)
print(q.data,q.next)

r=Node(10)
print(r.data,r.next)

# Create a Singly ll

n.next=p
p.next=q
q.next=r

# Create a Circular Singly ll
r.next=n

print(n.data,n.next)
print(p.data,p.next)
print(q.data,q.next)
print(r.data,r.next)
