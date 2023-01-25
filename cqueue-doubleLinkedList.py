class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
        self.front = None


class DlList:
    def __init__(self):
        self.head = None
        self.lenght = 0

    def enqueue(self, data):
        new_node = Node(data)
        if self.head is not None:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            self.lenght += 1
        elif self.head is None:
            self.head = new_node
            self.front = new_node
            self.lenght += 1

    def dequeue(self):
        if self.head is None:
            print("List is Empty")
            return False
        if self.lenght == 1:
            data = self.front.data
            self.front = None
            self.head = None
            self.lenght -= 1
            return data
        else:
            data = self.front.data
            self.front = self.front.prev
            self.front.next = None
            self.lenght -= 1
        return data

    def __repr__(self):
        _str = ""
        if self.head is None:
            return _str
        temp = self.head
        while temp.next:
            _str += str(temp.data) + "<->"
            temp = temp.next
        else:
            _str += str(temp.data)
        return _str


Dll = DlList()
Dll.enqueue(1)
print(Dll)
print(Dll.dequeue())
print(Dll)
print(Dll.lenght)
