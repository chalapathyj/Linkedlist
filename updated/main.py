#/*Importing modules Stack and Queue*/#
from Queue import qu
from Stack import st

#/*Start of Iterator function for stack and queue*/#
class DsItr:

    def __init__(self, ds):
        self.ds = ds.head

    def __iter__(self):
        return self

    def __next__(self):
        if self.ds is not None:
            data = self.ds.data
            self.ds = self.ds.nxt
            return data
        else:
            raise StopIteration()
#/*End of Iterator function for stack and queue*/#

#/*start of Polymorphism for displaying the contents*/#
def display(datastruct):
    datastruct.display()
#/*End of Polymorphism for displaying the contents*/#

#/*start of calling iterator on stack and queue*/#
def itrat(dsobj):
  for x in DsItr(dsobj):
    print (x)
#/*End of calling iterator on stack and queue*/#

#/*calling display function using Polymorphism on stack and queue*/"
display(st)
st.pop()
st.push(222)
display(qu)
qu.remove()
qu.add(333)
#/*End of calling display function using Polymorphism on stack and queue*/"
#/*calling iterator function on stack and queue*/#
print ("Start of iterator function on stack:")
itrat(st)
print ("End of iterator function on stack")
print ("Start of iterator function on queue:")
itrat(qu)
print ("End of iterator function on queue")
#/*End of calling iterator function on stack and queue*/#
