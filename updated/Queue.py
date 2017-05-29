#/* importing class list from double linked list*/
from DbleLkList import List

#/*defining class Queue*/
class Queue(List):
    QueSize = 0
    #/* defining method add to add elements to the linked list on tail */#
    def add(self, data):
        if self.isListEmpty():
            self._make_node(data)
        else:
            self.insertFront(None, data)
        self.QueSize += 1
    #/* End of defining method Push to add elements to the linked list on tail */#
    #/* defining method remove to remove elements to the linked list on tail */#
    def remove(self):
        if self.QueSize == 0:
            print("Queue is empty, add some values and try agaian!")
            return
        else:
            cur_node = self.tail
            print("removes a node from the Queue:", cur_node.data)
            if cur_node is not None:
                cur_node = self.tail = cur_node.prev
                cur_node.nxt = None

            else:
                print("List is empty")

        self.QueSize -= 1
    #/* End of defining method remove to remove elements to the linked list on tail */#
    #/* start of defining method is Queue empty or not */#
    def isQueEmpty(self):
        return bool(self.QueSize < 1)
    #/* End of defining method is Queue empty or not */#
    #/* start of defining method is Queue ful or not */#
    def isQueFull(self):
        return bool(self.QueSize >= 10)
    #/* End of defining method is Queue ful or not */#
    #/* start of defining method display ful or not */#
    def display(self):
        print("No of nodes in the Queue:",  self.QueSize)
        super(Queue, self).display() 

#/*End of defining class Queue*/

#/* creating an object to the class Queue 
qu = Queue()

#/* adding elements to the Queue */ #
qu.add(15)
qu.add(25)
qu.add(35)
qu.add(45)
qu.add(55)
qu.add(40)
qu.add(75)
qu.add(95)
qu.add(85)
#/*End of  adding elements to the Queue */ #

#/* testing queue scritp as a standalone */
if __name__ == "__main__":
  print("Is Queue Empty : ", qu.isQueEmpty())
  qu.display()
  print("Is Queue Empty : ", qu.isQueEmpty())
  print("Queue size: ", qu.QueSize)
  
  qu.remove()
  qu.remove()
  qu.remove()
  
  print("Queue size: ", qu.QueSize)
  print("Is Queue full : ", qu.isQueFull())
  
  qu.add(55)
  qu.add(22)
  qu.add(33)
  qu.add(44)
  qu.display()
  print("Queue size: ", qu.QueSize)
  print("Is Queue full : ", qu.isQueFull())
