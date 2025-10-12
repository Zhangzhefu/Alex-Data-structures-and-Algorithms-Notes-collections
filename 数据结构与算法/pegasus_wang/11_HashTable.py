# class Array(object):
#
#     def __init__(self, size=32, init=None):
#         self._size = size
#         self._items = [init] * size
#
#     def __getitem__(self, index):
#         return self._items[index]
#
#     def __setitem__(self, index, value):
#         self._items[index] = value
#
#     def __len__(self):
#         return self._size
#
#     def clear(self, value=None):
#         for i in range(len(self._items)):
#             self._items[i] = value
#         self._size = 0
#
#     def __iter__(self):
#         for item in self._items:
#             yield item
#
#
# class Slot(object):
#     """共有三种状态：
#         1. UNUSED 没被使用过的
#         2. EMPTY 只用过但被删除了
#         3. 槽正在被占用"""
#     def __init__(self, key, value):
#         self.key, self.value = key, value
#
#
# class HashTable(object):
#     UNUSED = None  # 未使用的
#     EMPTY = Slot(None, None)  # 使用过，但被删除了
#
#     def __init__(self):
#         self._table = Array(8, init=HashTable.UNUSED)  # 初始化时，大小永远是 2的n次方，每个元素都是未使用的
#         self.length = 0
#
#     @property
#     def _load_factor(self):
#         """返回一个能查看空间是否够用的值，
#         当空间不够时，根据装载因子新开空间并重新进行散列"""
#         return self.length / float(len(self._table))
#
#     def __len__(self):
#         return self.length
#
#     def _hash(self, key):
#         """得到数组的下表，来快速查找"""
#         return abs(hash(key)) % len(self._table)
#         # 使用内置 hash() 来获得整数并用其取模整表的长度
#
#     def _find_key(self, key):
#         index = self._hash(key)
#         _len = len(self._table)
#         while self._table[index] is not HashTable.UNUSED:  # 如果槽是 UNUSED 说明根本不存在
#             if self._table[index] is HashTable.EMPTY:
#                 index = (index * 5 + 1) % _len  # cpython 使用解决哈希冲突，继续到下一个槽
#                 continue
#             elif self._table[index].key == key:
#                 return index  # 直接返回下表
#             else:
#                 index = (index * 5 + 1) % _len  # 继续到下一个槽
#         return None  # 若什么都没找到，就返回 None
#
#     def _slot_can_insert(self, index):
#         """返回能使用的槽：UNUSED 或者 EMPTY"""
#         return self._table[index] is HashTable.UNUSED or self._table[index] is HashTable.EMPTY
#
#     def _find_slot_for_insert(self, key):
#         index = self._hash(key)
#         _len = len(self._table)
#         while not self._slot_can_insert(index):
#             index = (index*5 + 1) % _len  # 没找到的话，去下一个槽找
#         return index
#
#     def __contains__(self, key):
#         index = self._find_key(key)
#         return index is not None  # 找到了
#
#     def add(self, key, value):
#         if key in self:  # 如果有 key 了，就进行更新
#             index = self._find_key(key)
#             self._table[index].value = value
#             return False  # 并不增加，只更新
#         else:
#             index = self._find_slot_for_insert(key)
#             self._table[index] = Slot(key, value)
#             self.length += 1
#             if self._load_factor >= 0.8:
#                 self._rehash()
#             return True
#
#     def _rehash(self):
#         """先扩容并重新建表，然后重新插入值"""
#         old_table = self._table
#         resize = len(self._table) * 2
#         self._table = Array(resize, HashTable.UNUSED)
#         self.length = 0
#         # 到这里都是重新建表
#         # 从这里开始插入值
#         for slot in old_table:
#             if slot is not HashTable.UNUSED and slot is not HashTable.EMPTY:
#                 index = self._find_slot_for_insert(slot.key)
#                 self._table[index] = slot
#                 self.length += 1
#
#     def get(self, key, default=None):
#         index = self._find_key(key)
#         if index is None:
#             return default  # 要是没找到，将 default=None 返回
#         else:
#             return self._table[index].value  # 找到了，返回 value 值
#
#     def remove(self, key):
#         index = self._find_key(key)
#         if index is None:
#             raise KeyError()  # 如果没找到，返回 KeyError
#         value = self._table[index].value
#         self.length -= 1
#         self._table[index] = HashTable.EMPTY
#         return value
#
#     def __iter__(self):
#         """字典默认遍历 key 值"""
#         for slot in self._table:
#             if slot not in (HashTable.EMPTY, HashTable.UNUSED):
#                 yield slot.key
#
#
# def test_hash_table():
#     h = HashTable()
#     h.add('a', 0)
#     h.add('b', 1)
#     h.add('c', 2)
#     assert len(h) == 3
#     assert h.get('a') == 0
#     assert h.get('b') == 1
#     assert h.get('asdf') is None
#
#     h.remove('a')
#     assert h.get('a') is None
#     assert sorted(list(h)) == ['b', 'c']
#
#     n = 50
#     for i in range(n):
#         h.add(i, i)
#
#     for i in range(n):
#         assert h.get(i) == i

class Array(object):

    def __init__(self, size=32, init=None):
        self._size = size
        self._items = [init] * size

    def __getitem__(self, index):
        return self._items[index]

    def __setitem__(self, index, value):
        self._items[index] = value

    def __len__(self):
        return self._size

    def clear(self, value=None):
        for i in range(len(self._items)):
            self._items[i] = value
        self._size = 0

    def __iter__(self):
        for item in self._items:
            yield item


class Slot(object):
    def __init__(self, key, value):
        self.key, self.value = key, value


class HashTable(object):
    UNUSED = None
    EMPTY = Slot(None, None)

    def __init__(self):
        self._table = Array(8, init=HashTable.UNUSED)
        self.length = 0

    @property
    def _load_factor(self):
        return self.length / float(len(self._table))

    def __len__(self):
        return self.length

    def _hash(self, key):
        return abs(hash(key)) % len(self._table)

    def _find_key(self, key):
        index = self._hash(key)
        _len = len(self._table)
        while self._table[index] is not HashTable.UNUSED:
            if self._table[index] is HashTable.EMPTY:
                index = (index * 5 + 1) % _len
                continue
            elif self._table[index].key == key:
                return index
            else:
                index = (index * 5 + 1) % _len
        return None

    def _slot_can_insert(self, index):
        return self._table[index] is HashTable.EMPTY or self._table[index] is HashTable.UNUSED

    def _find_slot_for_insert(self, key):
        index = self._hash(key)
        _len = len(self._table)
        while not self._slot_can_insert(index):
            index = (index * 5 + 1) % _len
        return index

    def __contains__(self, key):
        index = self._find_key(key)
        return index is not None

    def add(self, key, value):
        if key in self:
            index = self._find_key(key)
            self._table[index] = value
            return False
        else:
            index = self._find_key(key)
            self._table[index] = Slot(key, value)
            self.length += 1
            if self._load_factor >= 0.8:
                self._rehash()
            return True

    def _rehash(self):
        old_table = self._table
        resize = len(self._table) * 2
        self._table = Array(resize, init=HashTable.UNUSED)
        self.length = 0

        for slot in old_table:
            if slot is not HashTable.UNUSED and slot is not HashTable.EMPTY:
                index = self._find_slot_for_insert(slot.key)
                self._table[index] = slot
                self.length += 1

    def get(self, key, default=None):
        index = self._find_key(key)
        if index is None:
            return default
        else:
            return self._table[index].value

    def remove(self, key):
        index = self._find_key(key)
        if index is None:
            raise KeyError
        value = self._table[index].value
        self.length -= 1
        self._table[index] = HashTable.UNUSED
        return value

    def __iter__(self):
        for slot in self._table:
            if slot not in (HashTable.UNUSED, HashTable.EMPTY):
                yield slot.key
