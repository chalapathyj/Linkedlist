from DbleLkList import List

newnde = List()
# print (newnde.isListEmpty())
# newnde._make_node(4)
# newnde.display()
# print(newnde.noOfNodes)

#newnde.insertFront(None, 5)
# newnde.insertAfter(4, 6)
# newnde.insertBack(6, 1)
# newnde.insertAfter(1, 3)
# newnde.insertFront(4, 1)
# print (newnde.isListEmpty())
# newnde.display()
# print("No of nodes: ", newnde.noOfNodes)


class Stack(List):

    def push(self, data):
        # self._make_node(4)
        if self.isListEmpty():
            Node = self._make_node(data)
            stackTop = stackBottom = Node

        else:
            Node = self.insertBack(None, data)
            stackTop.prev = Node
            stackTop = Node

    def pop(self, data):
        pass

    def isStackEmpty(self):
        pass

    def isStackFull(self):
        pass

    def display(self):
        pass

st = Stack()
st.push(5)
st.push(35)
st.push(25)
# st.push(5)
# st.push(65)
# st.push(45)
# st.push(95)
st.display()
