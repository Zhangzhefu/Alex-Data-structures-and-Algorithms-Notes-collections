class BSTNode(object):
    def __init__(self, key, value, left=None, right=None):
        self.key, self.value, self.left, self.right = key, value, left, right


class BinarySearchTree(object):
    def __init__(self, root=None):
        self.root = root


    @classmethod
    def build_from(cls, node_list):
        cls.size = 0
        key_to_node_dict = {}
        for node_dict in node_list:
            key = node_dict['key']
            key_to_node_dict[key] = BSTNode(key, value=key)

        for node_dict in node_list:
            key = node_dict['key']
            node = key_to_node_dict[key]
            if node_dict['is_root']:
                root = node
            node.left = key_to_node_dict.get(node_dict['left'])
            node.right = key_to_node_dict.get(node_dict['right'])
            cls.size += 1
        return cls(root)

    def _bst_search(self, subtree, key):
        """进入循环，如果 key 大于当前的值，就去右子树。小于，就去左子树。若等于就返回它"""
        if subtree is None:
            return None
        elif key < subtree.key:
            return self._bst_search(subtree.left, key)
        elif key > subtree.key:
            return self._bst_search(subtree.right, key)
        else:
            return subtree

    def get(self, key, default=None):
        """将需要找到的值发给 _bst_search 函数，若找到了·，返回它的值"""
        node = self._bst_search(self.root, key)
        if node is None:
            return default
        else:
            return node.value

    def __contains__(self, key):  # in operator
        return self._bst_search(self.root, key) is not None

    def _bst_min_node(self, subtree):
        """找到左子树里最小的值也就是，尽头的值 的辅助方法"""
        if subtree is None:
            return None
        elif subtree.left is None:  # 找到了左子树的尽头
            return subtree
        else:
            return self._bst_min_node(subtree.left)

    def bst_min(self):
        """找到左子树里最小的值"""
        node = self._bst_min_node(self.root)
        return node.value if node else None

    def _bst_insert(self, subtree, key, value):
        if subtree is None:
            subtree = BSTNode(key, value)
        elif key < subtree.key:
            subtree.left = self._bst_insert(subtree.left, key, value)
        elif key > subtree.key:
            subtree.right = self._bst_insert(subtree.right, key, value)
        return subtree

    def add(self, key, value):
        node = self._bst_search(self.root, key)
        if node is not None:
            node.value = value
            return False
        else:
            self.root = self._bst_insert(self.root, key, value)
            self.size += 1
            return True

    def _bst_remove(self, subtree, key):
        """predecessor(逻辑前任), successor(逻辑后任)，这两个是离被删除节点最近的两个值，
        后任比当前节点大，前任比当前节点小
        实际上，逻辑后任需要与被删除节点替换位置以保持二叉树的性质，
        而被替换出去的被删除节点不在被指向或指向其它节点来做到删除，因此后继节点有被删除节点的 key与它自己的值
        """
        if subtree is None:
            return None
        elif key < subtree.key:
            subtree.left = self._bst_remove(subtree.left, key)
            return subtree
        elif key > subtree.key:
            subtree.right = self._bst_remove(subtree.right, key)
        else:  # 找到了需要删除的节点
            if subtree.left is None and subtree.right is None:  # 说明这是叶子节点
                return None
            elif subtree.left is None or subtree.right is None:  # 有一个孩子
                if subtree.left is not None:  # 左孩子为空
                    return subtree.left  # 返回孩子，并且让父亲节点指过去
                else:
                    return subtree.right  # 返回孩子，并且让父亲节点指过去
            else:  # 俩孩子. 需要找到后继节点并替换
                successor_node = self._bst_min_node(subtree.right)
                subtree.key, subtree.value = successor_node.key, successor_node.value
                subtree.right = self._bst_remove(subtree.right, successor_node.key)
                return subtree

    def remove(self, key):
        assert key in self
        self.size -= 1
        return self._bst_remove(self.root, key)


NODE_LIST = [
    {'key': 60, 'left': 12, 'right': 90, 'is_root': True},
    {'key': 12, 'left': 4, 'right': 41, 'is_root': False},
    {'key': 4, 'left': 1, 'right': None, 'is_root': False},
    {'key': 1, 'left': None, 'right': None, 'is_root': False},
    {'key': 41, 'left': 29, 'right': None, 'is_root': False},
    {'key': 29, 'left': 23, 'right': 37, 'is_root': False},
    {'key': 23, 'left': None, 'right': None, 'is_root': False},
    {'key': 37, 'left': None, 'right': None, 'is_root': False},
    {'key': 90, 'left': 71, 'right': 100, 'is_root': False},
    {'key': 71, 'left': None, 'right': 84, 'is_root': False},
    {'key': 100, 'left': None, 'right': None, 'is_root': False},
    {'key': 84, 'left': None, 'right': None, 'is_root': False}
]


def test_bst_tree():
    bst = BinarySearchTree.build_from(NODE_LIST)
    for node_dict in NODE_LIST:
        key = node_dict['key']
        assert bst.get(key) == key

    assert bst.size == len(NODE_LIST)
    assert bst.get(-1) is None
    assert bst.bst_min() == 1
    bst.add(0, 0)
    assert bst.bst_min() == 0

    bst.remove(12)
    assert bst.get(12) is None

    bst.remove(29)
    assert bst.get(29) is None
