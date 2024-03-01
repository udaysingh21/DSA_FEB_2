class Node:
    def __init__(self,value):
        self.data=value
        self.next=None
        self.prev=None

n=Node(7)
print(n.data,n.next,n.prev)

p=Node(8)
print(p.data,p.next,n.prev)

q=Node(9)
print(q.data,q.next,n.prev)

r=Node(10)
print(r.data,r.next,n.prev)

# Create a Doubly ll

n.next=p
p.prev=n

p.next=q
q.prev=p

q.next=r
r.prev=q

# Create a Circular Doubly ll
r.next=n
n.prev=r

print(n.data,n.next,n.prev)
print(p.data,p.next,p.prev)
print(q.data,q.next,q.prev)
print(r.data,r.next,r.prev)
