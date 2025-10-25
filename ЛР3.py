import math
from collections import deque

# 1. Бинарная куча (min-heap)
class BinaryHeap:
    def __init__(self):
        self.heap = []
    
    def parent(self, i):
        return (i - 1) // 2
    
    def left_child(self, i):
        return 2 * i + 1
    
    def right_child(self, i):
        return 2 * i + 2
    
    def insert(self, key):
        self.heap.append(key)
        self._sift_up(len(self.heap) - 1)
    
    def extract_min(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._sift_down(0)
        return root
    
    def _sift_up(self, i):
        while i > 0 and self.heap[self.parent(i)] > self.heap[i]:
            self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]
            i = self.parent(i)
    
    def _sift_down(self, i):
        min_index = i
        n = len(self.heap)
        
        left = self.left_child(i)
        if left < n and self.heap[left] < self.heap[min_index]:
            min_index = left
        
        right = self.right_child(i)
        if right < n and self.heap[right] < self.heap[min_index]:
            min_index = right
        
        if i != min_index:
            self.heap[i], self.heap[min_index] = self.heap[min_index], self.heap[i]
            self._sift_down(min_index)

# 2. Биномиальная куча
class BinomialNode:
    def __init__(self, key):
        self.key = key
        self.degree = 0
        self.parent = None
        self.child = None
        self.sibling = None

class BinomialHeap:
    def __init__(self):
        self.head = None
    
    def merge(self, h2):
        # Объединение двух куч
        pass
    
    def insert(self, key):
        new_heap = BinomialHeap()
        new_node = BinomialNode(key)
        new_heap.head = new_node
        self.merge(new_heap)
    
    def extract_min(self):
        # Найти минимальный узел
        pass

# 3. Куча Фибоначчи (упрощенная версия)
class FibonacciHeap:
    def __init__(self):
        self.min_node = None
        self.count = 0
    
    def insert(self, key):
        new_node = BinomialNode(key)
        if self.min_node is None:
            self.min_node = new_node
        else:
            # Добавить в корневой список
            pass
        self.count += 1
    
    def extract_min(self):
        if self.min_node is None:
            return None
        min_node = self.min_node
        # Удалить минимальный узел и объединить деревья
        return min_node.key

# 4. Хеш-таблица с цепочками
class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]
    
    def _hash(self, key):
        return hash(key) % self.size
    
    def insert(self, key, value):
        index = self._hash(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)
                return
        self.table[index].append((key, value))
    
    def get(self, key):
        index = self._hash(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        return None
    
    def delete(self, key):
        index = self._hash(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                del self.table[index][i]
                return True
        return False

# Демонстрация
if __name__ == "__main__":
    print("=== Python Demo ===")
    
    # Бинарная куча
    bh = BinaryHeap()
    for num in [5, 3, 8, 1, 2]:
        bh.insert(num)
    print("Binary Heap extract_min:", bh.extract_min())
    
    # Хеш-таблица
    ht = HashTable()
    ht.insert("apple", 10)
    ht.insert("banana", 20)
    print("HashTable get apple:", ht.get("apple"))
