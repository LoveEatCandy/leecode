"""
运用你所掌握的数据结构，设计和实现一个  LRU (最近最少使用) 缓存机制。它应该支持以下操作： 获取数据 get 和 写入数据 put 。

获取数据 get(key) - 如果密钥 (key) 存在于缓存中，则获取密钥的值（总是正数），否则返回 -1。
写入数据 put(key, value) - 如果密钥不存在，则写入其数据值。当缓存容量达到上限时，它应该在写入新数据之前删除最近最少使用的数据值，从而为新的数据值留出空间。

进阶:

你是否可以在 O(1) 时间复杂度内完成这两种操作？

示例:

LRUCache cache = new LRUCache( 2 /* 缓存容量 */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // 返回  1
cache.put(3, 3);    // 该操作会使得密钥 2 作废
cache.get(2);       // 返回 -1 (未找到)
cache.put(4, 4);    // 该操作会使得密钥 1 作废
cache.get(1);       // 返回 -1 (未找到)
cache.get(3);       // 返回  3
cache.get(4);       // 返回  4
"""


class L:
    def __init__(self, key=None, val=None, pre=None, next=None):
        self.key = key
        self.val = val
        self.pre = pre
        self.next = next


class LRUCache:
    def __init__(self, capacity: int):
        self.head = L()
        self.end = L()
        self.head.next = self.end
        self.end.pre = self.head
        self.cache = {}
        self.capacity = capacity

    def remove_to_end(self, point):
        point.pre = self.end.pre
        point.next = self.end
        self.end.pre.next = point
        self.end.pre = point

    def get(self, key: int) -> int:
        if key in self.cache:
            value = self.cache[key]
            value.pre.next = value.next
            value.next.pre = value.pre
            self.remove_to_end(value)
            return value.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            v = self.cache[key]
            v.val = value
            v.pre.next = v.next
            v.next.pre = v.pre
            self.remove_to_end(v)
        else:
            new = L(key, value)
            self.remove_to_end(new)
            self.cache[key] = new
        if len(self.cache) > self.capacity:
            f = self.head.next
            self.cache.pop(f.key)
            self.head.next = f.next
            f.next.pre = self.head


# 时间O(1)，空间O(n)
