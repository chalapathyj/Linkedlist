#/* importing class list from double linked list*/
from DbleLkList import List

#/*defining class Stack*/
class Stack(List):
    StackSize = 0
    #/* defining class Push to add elements to the linked list on head */#
    def push(self, data):
        if self.isListEmpty():
            self._make_node(data)
        else:
            self.insertFront(None, data)
        self.StackSize += 1
    #/*End of defining class Push to add elements to the linked list on head */#
    #/* Start of defining class Pop to remove elements to the linked list on tail */#
    def pop(self):
        if self.StackSize == 0:
            print("Stack is empty, push some values and try agaian!")
            return
        else:
            cur_node = self.head
            print("pops a node from the stack:", cur_node.data)
            if cur_node is not None:
                cur_node = self.head = cur_node.nxt
                cur_node.prev = None

            else:
                print("List is empty")

        self.StackSize -= 1
    #/* End of defining class Pop to remove elements to the linked list on tail */#
    #/* checking whether the stack is empty or not */#
    def isStackEmpty(self):
        return bool(self.StackSize < 1)
    #/*End of  checking whether the stack is empty or not */#
    
    #/* checking whether the stack is Full or not */#
    def isStackFull(self):
        return bool(self.StackSize >= 10)
    #/*End of  checking whether the stack is Full or not */#
    #/* Displaying the stack */#
    def display(self):
        print("No of nodes in the stack:",  self.StackSize)
        super(Stack, self).display() 
    #/*End of  Displaying the stack */#    

#/*End of defining class Stack*/

#/* creating an object for stack and pushing the elements */#
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
#/* end of pushing elements on to stack.


#/* for testing if stack.py is executed as a stand alone */# 
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
#/*End of testing if stack.py is executed as a stand alone */#
