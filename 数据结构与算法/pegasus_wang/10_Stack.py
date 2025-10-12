# 栈

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


class Stack():
    def __init__(self):
        self.deque = Deque()

    def push(self, value):
        return self.deque.append(value)

    def pop(self):
        return self.deque.pop()

    def __len__(self):
        return len(self.deque)

    def is_empty(self):
        return len(self) == 0


def test_stack():
    s = Stack()
    for i in range(3):
        s.push(i)

    assert len(s) == 3
    assert s.pop() == 2
    assert s.pop() == 1
    assert s.pop() == 0

    assert s.is_empty()

    import pytest
    with pytest.raises(Exception) as excinfo:
        s.pop()
    assert 'empty' in str(excinfo.value)

# Stack overflow
# def infinite_fib(n):
#     return infinite_fib(n-1) + infinite_fib(n-2)
#
#
# if __name__ == '__main__':
#     infinite_fib(10)
# 没有递归出口的函数
