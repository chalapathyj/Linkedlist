from DbleLkList import List

class Stack(List):
    StackSize = 0

    def push(self, data):
        if self.isListEmpty():
            self._make_node(data)
        else:
            self.insertFront(None, data)
        self.StackSize += 1

    def pop(self):
        if self.StackSize == 0:
            print("Stack is empty, push some values and try agaian!")
            return
        else:
            cur_node = self.head
            print("pops a node from the stack:", cur_node.data)
            if cur_node is not None:
                cur_node = self.head = cur_node.next
                cur_node.prev = None

            else:
                print("List is empty")

        self.StackSize -= 1

    def isStackEmpty(self):
        return bool(self.StackSize < 1)

    def isStackFull(self):
        return bool(self.StackSize >= 10)

    def display(self):
        print("No of nodes in the stack:",  self.StackSize)
        super(Stack, self).display() 
        

st = Stack()


st.push(5)
st.push(35)
st.push(25)
st.push(5)
st.push(65)
st.push(45)
st.push(95)
st.push(65)
st.push(45)

if __name__ == "__main__":
  print("Is stack Empty : ", st.isStackEmpty())
  st.display()
  print("Is stack Empty : ", st.isStackEmpty())
  print("Stack size: ", st.StackSize)
  
  st.pop()
  st.pop()
  st.pop()
  
  print("Stack size: ", st.StackSize)
  print("Is stack full : ", st.isStackFull())
  
  st.push(55)
  st.push(22)
  st.push(33)
  st.push(44)
  st.display()
  print("Stack size: ", st.StackSize)
  print("Is stack full : ", st.isStackFull())
