class Node():
    def __init__(self, data = None):
        self._data = data
        self._next = None
        self._prev = None

    def __str__(self):
        return '{}'.format(self._data)

class List():
    def __init__(self):
        self._begin = None
        self._end = None


    def isEmpty(self):
        if self._begin == None:
            return True
        return False


    def insertEnd(self, data = None):
        newnode = Node(data)

        if self.isEmpty():
            self._begin = self._end = newnode
        else:
            newnode._prev = self._end
            self._end._next = newnode
            self._end = newnode

    def search(self, x):
        i = self._begin
        while i != None:
            if x == i._data:
                break
            else:
                i = i._next
        return i

    def removeElement(self, x):
        found_node = self.search(x)
        if found_node != None:
            if found_node._prev != None:
                found_node._prev._next = found_node._next
            else:
                self._begin = found_node._next
            if found_node._next != None:
                found_node._next._prev = found_node._prev
            else:
                self._end = found_node._prev

        return found_node


    def removeFromBegin(self):
        node = self._begin
        if not self.isEmpty():
            if node._next == None:
                self._end = None
            else:
                node._next._prev = None
            self._begin = node._next
        return node

    def __str__(self):
        s = ''
        i = self._begin
        while i != None:
            s += '{} '.format(i)
            i = i._next
        return s


class Queue(List):
    def insert(self, data):
        self.insertEnd(data)

    def remov(self, data):
        return self.removeFromBegin()


class Stack(List):
    def Push(self, data=None):
        newnode = Node(data)
        if self.isEmpty():
            self._end = newnode
        else:
            newnode._next = self._begin
            self._begin._prev = newnode
        self._begin = newnode

    def Pop(self):
        return self.removeFromBegin()


n = int(input())
queue1 = input().split()
queue = Queue()
for i in queue1:
    queue.insertEnd(i)
r = int(input())
toremove = input().split()
for x in toremove:
    queue.removeElement(x)

print(queue)