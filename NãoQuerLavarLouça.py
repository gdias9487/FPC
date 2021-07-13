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


def game(n):
    for i in range(n):
        deck_in_desk = List()
        player_deck = List()
        count = 0
        winner = 0
        players = List()
        desk = input().split()
        for i in desk:
            deck_in_desk.insertEnd(i)
        while True:
            decks = [x for x in input().split()]
            if decks[0] == '-1':
                break
            for i in decks:
                player_deck.insertEnd(i)
            players.insertEnd(player_deck)
            player_deck = List()
        while True:
            if count > 1000:
                print('0')
                break
            elif winner != 0:
                print(winner)
                break
            deck_top = deck_in_desk.first()
            for i, c in enumerate(players):
                if c.isEmpty():
                    winner = i + 1
                    break
                else:
                    top = c.first()
                    if top == deck_top:
                        c.removeFromBegin()
                    else:
                        c.removeFromBegin()
                        c.insertEnd(top)
            deck_in_desk.removeFromBegin()
            deck_in_desk.insertEnd(deck_top)
            count += 1
        deck_in_desk = List()
    return


n = int(input())
game(n)
