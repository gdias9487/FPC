class Node():
    def __init__(self, data=None):
        self._data = data
        self._next = None
        self._prev = None

    def getdata(self):
        return self._data

    def getnext(self):
        return self._next


class List():
    def __init__(self):
        self._begin = None
        self._end = None

    def first(self):
        return self._begin.getdata()

    def isEmpty(self):
        if self._begin == None:
            return True
        return False

    def insertEnd(self, data=None):
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

    def Reset(self):
        self._begin = self._end = None

    def lenght(self):
        node = self._begin
        len = 0
        while node != None:
            node = node._next
            len += 1
        return len

    def __str__(self):
        s = ''
        i = self._begin
        while i != None:
            s += '{} '.format(i.getdata())
            i = i.getnext()
        return s

    def __iter__(self):
        i = self._begin
        while i != None:
            yield i._data
            i = i._next


n = int(input())
D, E = List(), List()
result = 0
for i in range(n):
    boots = input().split()
    if boots[1] == 'E':
        E.insertEnd(boots[0])
    else:
        D.insertEnd(boots[0])

for i in D:
    if i in E:
        result += 1
        E.removeElement(i)
print(result)
