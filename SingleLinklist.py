class Node:
    noOfNodes = 0

    def __init__(self, data, prev=None, nxt=None):
        self.data = data
        self.prev = prev
        self.next = nxt
        self.noOfNodes += 1


class List:
	head = None
	tail = None
    def _make_node(self, data):
    	node = Node(data)
        if self.head is None:
            self.head = self.tail = node
        else:
        	node.prev = self.tail
        	node.next = None
        	self.tail.next = self.tail = node
        	self.tail = node
        self.noOfNodes += 1

    def insert_after(self, ptr=None, data):
        if ptr is None:
            self._make_node(data)
        else:

    def show(self):
        return (self.prev, self.data, self.next)


newnde = List()
newnde.make_node(4)
print(newnde.show())
print(newnde.noOfNodes)
