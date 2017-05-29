#/* start of creating Node class */#
class Node:

    def __init__(self, data, prev=None, nxt=None):
        self.data = data
        self.prev = prev
        self.nxt = nxt

#/* End of creating Node class */#
#/* start of creating Double Linked list class */#
class List:
    #/*class varible no of Nodes*/
    noOfNodes = 0
    #/*constructor having head and tail as instance variable
    def __init__(self):
      self.head = None
      self.tail = None

    #/*Creating a node using _make_node method as private*/
    def _make_node(self, data):
        try:
            node = Node(data)
            if self.head is None:
                self.head = self.tail = node
                node.prev = None
                node.nxt = None

            self.noOfNodes += 1
            return node
        except:
            print("Failed to create the node")
    #/*End of creating a node using _make_node method as private*/
    
    #/* insertAfter function not sure it is useful. Doubt not clarified*/
    # def insertAfter(self, ptr, data):

    #     def nodeSwitch(cur_node):
    #         node = self._make_node(data)
    #         if cur_node is self.tail:
    #             cur_node.nxt = self.tail = node
    #             node.prev = cur_node
    #             node.nxt = None

    #         elif cur_node is self.head:
    #             cur_node.prev = self.head = node
    #             node.nxt = cur_node
    #             node.prev = None

    #         return node
    #     if isinstance(ptr, Node):
    #         nodeSwitch(ptr)
    #         return

    #     while cur_node is not None:
    #         if cur_node.data == ptr:
    #             nodeSwitch(cur_node)
    #             break
    #         cur_node = cur_node.nxt
    #     else:
    #         print("Node %s is not found in the list" % ptr)
        #raise Exception("Node %d is not found in the list" % ptr)
#/* End of insertAfter function not sure it is useful. Doubt not clarified*/
    #/* start of insertFront for inserting function to the head of the linked list */
    def insertFront(self, ptr, data):
        if ptr is None:
            cur_node = self.head
        elif not isinstance(ptr, Node):
            raise Exception("Invalid parameter, pointer is expected")

        #self.insertAfter(cur_node, data)
        node = self._make_node(data)
        cur_node.prev = self.head = node
        node.nxt = cur_node
        node.prev = None
    #/* End of insertFront for inserting function to the head of the linked list */
    
    #/* start of insertBack for inserting function to the tail of the linked list */
    def insertBack(self, ptr, data):
        if ptr is None:
            cur_node = self.tail
        elif not isinstance(ptr, Node):
            raise Exception("Invalid parameter, pointer is expected")
        
        #self.insertAfter(cur_node, data)
        node = self._make_node(data)
        cur_node.nxt = self.tail = node
        node.prev = cur_node
        node.nxt = None
    #/* End of insertBack for inserting function to the tail of the linked list */
    
    #/* start of checking list is empty function of the linked list */
    def isListEmpty(self):
        return bool(self.head is None)
    #/* End of checking list is empty function of the linked list */
    
    #/* start of displaying nodes of the linked list */
    def display(self):
        cur_node = self.head
        while cur_node is not None:
            print("showing node :", cur_node.data)
            cur_node = cur_node.nxt
    #/* End of displaying nodes of the linked list */

#/*for checking whether the double linked list is working */
# newnde = List()
# print (newnde.isListEmpty())
# newnde._make_node(4)
# newnde.display()
# print(newnde.noOfNodes)

# #newnde.insertFront(None, 5)
# newnde.insertBack(None, 1)
# newnde.insertFront(None, 1)
# print (newnde.isListEmpty())
# newnde.display()

#/*End of for checking whether the double linked list is working */
