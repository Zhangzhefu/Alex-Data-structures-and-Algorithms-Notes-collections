class Node(object):
    def __init__(self, value=None, next=None):
        self.value, self.next = value, next


class FullError(Exception):
    pass


class EmptyError(Exception):
    pass


class Queue(object):
    def __init__(self, maxsize=None):
        self.maxsize = maxsize
        self.length = 0
        self.root = Node()
        self.tailnode = None

    def __len__(self):
        return self.length

    def push(self, value):
        if self.maxsize is not None and len(self) >= self.maxsize:
            raise FullError("Queue Full")
        node = Node(value)
        tailnode = self.tailnode

        if tailnode is None:
            self.root.next = node
        else:
            tailnode.next = node
        self.tailnode = node
        self.length += 1

    def pop(self):
        if len(self) <= 0:
            return EmptyError("Queue Empty")
        headnode = self.root.next
        self.root.next = headnode.next
        self.length -= 1
        value = headnode.value

        if self.tailnode is headnode:
            self.tailnode = None
        del headnode
        return value


def test_queue():
    q = Queue()
    q.push(1)
    q.push(2)
    q.push(3)

    # assert len(q) == 3
    #
    # assert q.pop() == 1
    # assert q.pop() == 2
    # assert q.pop() == 3

