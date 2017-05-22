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

            self.noOfNodes += 1
            return node
        except:
            print("Failed to create the node")
            return None

    def insertAfter(self, ptr, data):
        cur_node = self.head

        def nodeSwitch(cur_node):
            node = self._make_node(data)
            if cur_node.nxt is None:
                cur_node.nxt = self.tail = node
                node.prev = cur_node
                node.nxt = None
            elif cur_node.prev is None:
                cur_node.prev = self.head = node
                node.nxt = cur_node
                node.prev = None
            else:
                cur_node.nxt = cur_node.nxt.prev = node
                node.prev = cur_node
                node.nxt = cur_node.nxt.prev
            return node
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
        if ptr is None:
            cur_node = self.head
        elif not isinstance(ptr, Node):
            raise Exception("Invalid parameter, pointer is expected")
        try:
            self.insertAfter(cur_node, data)
        except:
            pass

    def insertBack(self, ptr, data):
        if ptr is None:
            cur_node = self.tail
        elif not isinstance(ptr, Node):
            raise Exception("Invalid parameter, pointer is expected")
        try:
            self.insertAfter(cur_node, data)
        except:
            pass

    def isListEmpty(self):
        if self.head is not None:
            return False
        else:
            return True

    def display(self):
        cur_node = self.head
        while cur_node is not None:
            print("showing node :", cur_node.data)
            cur_node = cur_node.nxt

# newnde = List()
# print (newnde.isListEmpty())
# newnde._make_node(4)
# newnde.display()
# print(newnde.noOfNodes)

# #newnde.insertFront(None, 5)
# newnde.insertAfter(4, 6)
# newnde.insertBack(6, 1)
# newnde.insertAfter(1, 3)
# newnde.insertFront(3, 1)
# print (newnde.isListEmpty())
# newnde.display()
