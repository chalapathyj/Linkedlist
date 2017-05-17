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

            List.noOfNodes += 1
            return node
        except:
            raise "Failed to create the node"

    def insert_after(self, data, ptr=None):
        if ptr is None:
            print("Calling make_node")
            self._make_node(data)
        else:
            node = self._make_node(data)
            cur_node = self.head
            while cur_node is not None:
                if cur_node.data == ptr:
                    node.nxt = cur_node.nxt
                    cur_node.prev = node
                    cur_node.nxt = node
                    node.prev = cur_node
                    print("Node")
                    break
                cur_node = cur_node.nxt

    def show(self):
        cur_node = self.head
        while cur_node is not None:
            print("showing node :", cur_node.data)
            cur_node = cur_node.nxt


newnde = List()
newnde.insert_after(4)
newnde.show()
print(newnde.noOfNodes)
newnde.insert_after(5, 4)
newnde.insert_after(6, 4)
newnde.insert_after(3, 6)
newnde.insert_after(1, 5)
newnde.show()
print("No of nodes: ", newnde.noOfNodes)
