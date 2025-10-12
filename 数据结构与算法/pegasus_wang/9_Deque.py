# 双端队列

class Node(object):
    def __init__(self, value=None, prev=None, next=None):
        self.value, self.prev, self.next = value, prev, next


class DoubleLinkedList(object):
    def __init(self, maxsize=None):
        self.maxsize = maxsize
        node = Node()
        self.root = node
        node.next, node.prev = node, node
        self.length = 0

    def __len__(self):
        return self.length

    def headnode(self):
        return self.root.next

    def tailnode(self):
        return self.root.prev

    def append(self, value):
        if self.maxsize is not None and len(self) > self.maxsize:
            raise Exception("Full")
        node = Node(value=value)
        tailnode = self.tailnode()

        tailnode.next = node
        node.prev = tailnode
        self.root.prev = node
        node.next = self.root
        self.length += 1

    def remove(self, node):
        if node is self.root:
            return
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
        self.length -= 1
        return node


class Deque(DoubleLinkedList):

    def pop(self):
        if len(self) == 0:
            raise Exception("empty")
        tailnode = self.tailnode()
        value = tailnode.value
        self.remove(tailnode)
        return value

    def popleft(self):
        if len(self) == 0:
            raise Exception("empty")
        headnode = self.headnode()
        value = headnode.value
        self.remove(headnode)
        return value
