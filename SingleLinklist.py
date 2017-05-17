class Node:

    def __init__(self, data, prev=None, nxt=None):
        self.data = data
        self.prev = prev
        self.nxt = nxt


class List:
    head = None
    tail = None
    noOfNodes = 0

    def _make_node(self, data):
        try:
            node = Node(data)
            if self.head is None:
                self.head = self.tail = node
                self.prev = None
                self.nxt = None
            else:
                self.prev = self.tail.data
                self.tail = node
                self.nxt = None
                

            self.noOfNodes += 1
            return node
        except:
            raise Exception("Failed to create the node")

    def insertAfter(self, ptr, data):
        cur_node = self.head

        def nodeSwitch(cn):
            node = self._make_node(data)
            node.nxt = cn.nxt
            cn.nxt = node
            node.prev = cn

        if isinstance(ptr, Node):
            nodeSwitch(ptr)
            return

        while cur_node is not None:
            if cur_node.data == ptr:
                nodeSwitch(cur_node)
                break
            cur_node = cur_node.nxt
        else:
            print("Node %d is not found in the list" % ptr)
            #raise Exception("Node %d is not found in the list" % ptr)

    def insertFront(self, ptr, data):
        cur_node = self.head
        while cur_node is not None:
            if cur_node.data == ptr:
                if cur_node.prev is None:
                    node = self._make_node(data)
                    cur_node.prev = self.head = node
                    node.nxt = cur_node
                    node.prev = None
                else:
                    self.insertAfter(cur_node.prev, data)
                break
            cur_node = cur_node.nxt
        else:
            print("Node %d is not found in the list" % ptr)
            #raise Exception("Node %d is not found in the list" % ptr)

    def insertBack(self, ptr, data):
        cur_node = self.head
        while cur_node is not None:
            if cur_node.data == ptr:
                if cur_node.nxt is None:
                    node = self._make_node(data)
                    cur_node.prev = self.head = node
                    node.nxt = cur_node
                    node.prev = None
                else:
                    self.insertAfter(cur_node.next, data)
                
                break
            cur_node = cur_node.nxt
        else:
            print("Node %d is not found in the list" % ptr)
            #raise Exception("Node %d is not found in the list" % ptr)

    def show(self):
        cur_node = self.head
        while cur_node is not None:
            print("showing node :", cur_node.data)
            cur_node = cur_node.nxt


newnde = List()
newnde._make_node(4)
# newnde.insert_after(4)
newnde.show()
print(newnde.noOfNodes)
#newnde.insert_after(3, 5)
newnde.insertAfter(4, 5)
newnde.insertAfter(4, 6)
newnde.insertAfter(4, 3)
newnde.insertFront(3, 1)
newnde.show()
print("No of nodes: ", newnde.noOfNodes)
