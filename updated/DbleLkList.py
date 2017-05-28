class Node:

    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next


class List:
    head = None
    tail = None
    noOfNodes = 0

    def _make_node(self, data):
        try:
            node = Node(data)
            if self.head is None:
                self.head = self.tail = node
                node.prev = None
                node.next = None

            self.noOfNodes += 1
            return node
        except:
            print("Failed to create the node")

    # def insertAfter(self, ptr, data):

    #     def nodeSwitch(cur_node):
    #         node = self._make_node(data)
    #         if cur_node is self.tail:
    #             cur_node.next = self.tail = node
    #             node.prev = cur_node
    #             node.next = None

    #         elif cur_node is self.head:
    #             cur_node.prev = self.head = node
    #             node.next = cur_node
    #             node.prev = None

    #         return node
    #     if isinstance(ptr, Node):
    #         nodeSwitch(ptr)
    #         return

    #     while cur_node is not None:
    #         if cur_node.data == ptr:
    #             nodeSwitch(cur_node)
    #             break
    #         cur_node = cur_node.next
    #     else:
    #         print("Node %s is not found in the list" % ptr)
        #raise Exception("Node %d is not found in the list" % ptr)

    def insertFront(self, ptr, data):
        if ptr is None:
            cur_node = self.head
        elif not isinstance(ptr, Node):
            raise Exception("Invalid parameter, pointer is expected")
        try:
            #self.insertAfter(cur_node, data)
            node = self._make_node(data)
            cur_node.prev = self.head = node
            node.next = cur_node
            node.prev = None
        except:
            pass

    def insertBack(self, ptr, data):
        if ptr is None:
            cur_node = self.tail
        elif not isinstance(ptr, Node):
            raise Exception("Invalid parameter, pointer is expected")
        try:
            #self.insertAfter(cur_node, data)
            node = self._make_node(data)
            cur_node.next = self.tail = node
            node.prev = cur_node
            node.next = None
        except:
            pass

    def isListEmpty(self):
        return bool(self.head is None)
        # if self.head is not None:
        # return False
        # else:
        # return True

    def display(self):
        cur_node = self.head
        while cur_node is not None:
            print("showing node :", cur_node.data)
            cur_node = cur_node.next

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
