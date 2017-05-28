from Queue import qu
from Stack import st


class DS:

    def __init__(self, ds):
        self.ds = ds

    def __iter__(self):
        return self

    def next(self):
        if self.ds.next is not None:
            self.ds = self.ds.next
            return self.ds
        else:
            raise StopIteration()


def display(datastruct):
    datastruct.display()

display(st)
st.pop()
display(st)
#for x in DS(st):
    #print (x.data)
# st1 = Stack()
# qu1 = Queue()


# st1.push(5)
# st1.push(35)
# st1.push(25)
# st1.push(5)
# st1.push(65)
# st1.push(45)
# st1.push(95)
# st1.push(65)
# st1.push(45)

# st1.display()

# qu1.add(5)
# qu1.add(35)
# qu1.add(25)
# qu1.add(5)
# qu1.add(65)
# qu1.add(45)
# qu1.add(95)
# qu1.add(65)
# qu1.add(45)

# qu1.display()
