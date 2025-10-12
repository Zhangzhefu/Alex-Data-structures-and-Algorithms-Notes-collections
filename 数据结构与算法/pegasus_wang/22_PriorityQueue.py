# Queue: First in First out

class Array(object):

    def __init__(self, size=32):
        self._size = size
        self._items = [None] * size  # The use of *, make a list that is the size of "size"

    def __getitem__(self, index):
        return self._items[index]

    def __setitem__(self, index, value):
        self._items[index] = value

    def clear(self, value=None):
        for i in range(len(self._items)):
            self._items[i] = value

    def __len__(self):
        return self._size

    def __iter__(self):
        for item in self._items:
            yield item


class MaxHeap(object):
    def __init__(self, maxsize=None):
        self.maxsize = maxsize
        self._elements = Array(maxsize)
        self._count = 0

    def __len__(self):
        return self._count

    def add(self, value):
        if self._count > self.maxsize:
            raise Exception("Full")
        self._elements[self._count] = value
        self._count += 1
        self._siftup(self._count - 1)

    def _siftup(self, index):
        """上山操作，如果子节点比父母节点大，将两者调换"""
        if index > 0:
            parent = int((index - 1) / 2)
            if self._elements[index] > self._elements[parent]:
                self._elements[index], self._elements[parent] = self._elements[parent], self._elements[index]
                self._siftup(parent)

    def extract(self):
        """提取并拿掉根节点"""
        if self._count <= 0:
            raise Exception('empty')
        value = self._elements[0]
        self._count -= 1
        self._elements[0] = self._elements[self._count]
        self._siftdown(0)
        return value

    def _siftdown(self, index):
        """下山操作，判断右左孩子谁打，若其中一个子节点比父母节点大，将两者调换"""
        left = 2 * index + 1
        right = 2 * index + 2
        largest = index

        if (left < self._count and  # 有左孩子
                self._elements[left] >= self._elements[largest] and  # 左孩子比当前最大孩子大
                self._elements[left] >= self._elements[right]):  # 左孩子比右孩子大
            largest = left
        elif right < self._count and self._elements[right] >= self._elements[largest]:  # 有右孩子， 并且有孩子最大
            largest = right

        if largest != index:  # 若两者不一样，将其交换
            self._elements[largest], self._elements[index] = self._elements[index], self._elements[largest]
            self._siftdown(largest)  # 递归操作


def test_priority_queue():
    size = 5
    pq = PriorityQueue(size)
    pq.push(5, 'purple')
    pq.push(0, 'white')
    pq.push(3, 'orange')
    pq.push(1, 'black')

    res = []
    while not pq.is_empty():
        res.append(pq.pop())
    assert res == ['purple', 'orange', 'black', 'white']


class PriorityQueue(object):
    def __init__(self, maxsize=None):
        self.maxsize = maxsize
        self._maxheap = MaxHeap(maxsize)

    def push(self, priority, value):
        entry = (priority, value)
        self._maxheap.add(entry)

    def pop(self, with_priority=False):
        entry = self._maxheap.extract()
        if with_priority:
            return entry
        else:
            return entry[1]

    def is_empty(self):
        return len(self._maxheap) == 0
