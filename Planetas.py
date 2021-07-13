class Hash_Table:
    def __init__(self, n):
        self._lenght = n
        self._items = [None] * n
        self._values = [None] * n

    def gettable(self):
        return self._items

    def hashfunction(self, key):
        h = int(key, 2) % self._lenght
        return h

    def insertintable(self, key):
        i = self.hashfunction(key)
        self._items[i] = key
        self._values[i] = 1
        return None

    def search(self, key):
        i = self.hashfunction(key)
        if self._items[i] is None:
            return False
        else:
            return self._items[i]

    def addinvalue(self, val, key):
        i = self.hashfunction(key)
        if self.search(key) is not False:
            self._values[i] += val
        return self._values[i]

    def getvalue(self, key):
        i = self.hashfunction(key)
        if self.search(key) is not False:
            return self._values[i]


def greater(a, b):  # Função máximo
    return (a + b + absolute(a - b)) // 2


def absolute(a):
    if a > 0:
        return a
    else:
        return -a


max = 0
M, N = [int(x) for x in input().split()]
plans = [[None for i in range(4)] for j in range(M)]
regions = Hash_Table(20001)

for i in range(M):
    plans[i][0], plans[i][1], plans[i][2], plans[i][3] = [int(x) for x in input().split()]

for i in range(N):
    key = ''
    X, Y, Z = [int(x) for x in input().split()]
    for j in range(M):
        if plans[j][0] * X + plans[j][1] * Y + plans[j][2] * Z > plans[j][3]:
            key += '0'
        else:
            key += '1'

    if key == regions.search(key):
        regions.addinvalue(1, key)
    else:
        regions.insertintable(key)

    max = greater(regions.getvalue(key), max)

print(max)
