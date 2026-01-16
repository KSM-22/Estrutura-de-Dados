class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

node1 = Node('A')
node2 = Node('B')
node3 = Node('C')
node4 = Node('D')

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node1

node1.prev = None
node2.prev = node1
node3.prev = node2
node4.prev = node3

print(node1.data, node1, node1.next, node1.prev)
print(node2.data, node2, node2.next, node2.prev)
print(node3.data, node3, node3.next, node3.prev)
print(node4.data, node4, node4.next, node4.prev)

head = node1
current = head
number = 0
while current and number != 10:
    if not current.next or number == 9:
        print(current.data)
        break
    print(current.data, end=' --> ')
    current = current.next
    number += 1

print()
tail = node4
current = tail
while current:
    if not current.prev:
        print(current.data)
        break
    print(current.data, end=' --> ')
    current = current.prev
