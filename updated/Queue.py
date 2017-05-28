from DbleLkList import List

class Queue(List):
    QueSize = 0

    def add(self, data):
        if self.isListEmpty():
            self._make_node(data)
        else:
            self.insertFront(None, data)
        self.QueSize += 1

    def remove(self):
        if self.QueSize == 0:
            print("Queue is empty, add some values and try agaian!")
            return
        else:
            cur_node = self.tail
            print("removes a node from the Queue:", cur_node.data)
            if cur_node is not None:
                cur_node = self.tail = cur_node.prev
                cur_node.next = None

            else:
                print("List is empty")

        self.QueSize -= 1

    def isQueEmpty(self):
        return bool(self.QueSize < 1)

    def isQueFull(self):
        return bool(self.QueSize >= 10)

    def display(self):
        print("No of nodes in the Queue:",  self.QueSize)
        super(Queue, self).display() 


qu = Queue()


qu.add(5)
qu.add(35)
qu.add(25)
qu.add(5)
qu.add(65)
qu.add(45)
qu.add(95)
qu.add(65)
qu.add(45)

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
