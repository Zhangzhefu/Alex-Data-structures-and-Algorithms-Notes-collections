# def print_num_recursion(n):
#     if n == 0:
#         return 1
#     else:
#         print_num_recursion(n-1)
#         print(n)
#
#
# print_num_recursion(10)
"""
这里传进去的数字是10，因为10大于0，所以先执行 print_num_recursion(n-1) 操作
也就是 10-1 = 9，9还是大于0，所以还是先执行 print_num_recursion(n-1) 进入 8，
以此类推直到0，这时它返回1。然后打印 1，2，3... 9，10
"""


# def print_num_reverse(n):
#     if n == 0:
#         return 1
#     else:
#         print(n)
#         print_num_reverse(n-1)
#
#
# print_num_reverse(10)


"""
这里用相反的的概念，先打印，在执行 print_num_reverse(n-1) 操作，所以打印出来的就是 10，9，8 ... 2，1
"""
#
# import collections
# from collections import deque
#
#
# class Stack(object):
#     def __init__(self):
#         self._deque = collections.deque()
#
#     def push(self, value):
#         return self._deque.append(value)
#
#     def pop(self):
#         return self._deque.pop()
#
#     def is_empty(self):
#         return len(self._deque) == 0
#
#
# def print_num_use_stack(n):
#     """运用栈的简单递归"""
#     s = Stack()
#     while n > 0:
#         s.push(n)
#         n -= 1
#
#     while not s.is_empty():
#         print(s.pop())
#
#
# print_num_use_stack(10)
"""
当给一个递归数值的时候，它的算法是算出当前给的数值 x 加上 x-1
这时，它会往前退一个数，假设 x=5 那么，它就会设 x=4 同样使用 x + (x-1) 的算法它就会往前推到 x=3
这样一直往前退，直到 x=0，因为我设定了 x==0 时结束递归，所以它会使用 0 + 1 也就是 x=1 的值
然后 1 + 2也就是 x=2 的值，一直到 x=5。

整体原理就是，要想计算 x，就先找到 x-1 直到 0，这样计算回来。-1 就是递归出口
"""


def hanoi_move(n, source, dest, inter):
    if n >= 1:
        hanoi_move(n-1, source, inter, dest)
        print("move %s -> %s" % (source, dest))
        hanoi_move(n-1, inter, dest, source)


hanoi_move(3, "A", "C", "B")
# 1. 移动 n-1 个小盘子从左边到中间
# 2. 移动 第 n 个盘子从左到右边
# 3. 移动 n-1 个 小盘子从中间到右边
