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

    def findNode(self, ptr, data):
        cur_n = self.head
        while cur_n is not None:
            if cur_n.data == ptr:
                node = self._make_node(data)
                return (cur_n, node)
            cur_n = cur_n.nxt
        else:
             print("Node %d is not found in the list" % ptr)

    def insertAfter(self, ptr, data):
        cur_node = self.head

        def nodeSwitch(cur_node):
            node = self._make_node(data)
            node.nxt = cur_node.nxt
            cur_node.nxt = node
            node.prev = cur_node

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
                    cur_node.nxt = self.tail = node
                    node.nxt = None
                    node.prev = cur_node
                else:
                    self.insertAfter(cur_node, data)

                break
            cur_node = cur_node.nxt
        else:
            print("Node %d is not found in the list" % ptr)
        #raise Exception("Node %d is not found in the list" % ptr)

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



