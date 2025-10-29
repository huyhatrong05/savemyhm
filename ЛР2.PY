from collections import deque
import heapq
from typing import Any, List

# 1. Мультисписок (список списков)
class MultiList:
    def __init__(self):
        self.lists = []
    
    def add_list(self, lst: List[Any]):
        self.lists.append(lst)
    
    def get_all_elements(self) -> List[Any]:
        result = []
        for lst in self.lists:
            result.extend(lst)
        return result
    
    def __str__(self):
        return str(self.lists)

# 2. Очередь (на основе deque)
class Queue:
    def __init__(self):
        self.queue = deque()
    
    def enqueue(self, item: Any):
        self.queue.append(item)
    
    def dequeue(self) -> Any:
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.queue.popleft()
    
    def is_empty(self) -> bool:
        return len(self.queue) == 0
    
    def size(self) -> int:
        return len(self.queue)
    
    def __str__(self):
        return str(list(self.queue))

# 3. Дек (двусторонняя очередь)
class Deque:
    def __init__(self):
        self.deque = deque()
    
    def add_front(self, item: Any):
        self.deque.appendleft(item)
    
    def add_rear(self, item: Any):
        self.deque.append(item)
    
    def remove_front(self) -> Any:
        if self.is_empty():
            raise IndexError("Deque is empty")
        return self.deque.popleft()
    
    def remove_rear(self) -> Any:
        if self.is_empty():
            raise IndexError("Deque is empty")
        return self.deque.pop()
    
    def is_empty(self) -> bool:
        return len(self.deque) == 0
    
    def size(self) -> int:
        return len(self.deque)
    
    def __str__(self):
        return str(list(self.deque))

# 4. Приоритетная очередь
class PriorityQueue:
    def __init__(self):
        self.heap = []
        self.counter = 0  # для обработки одинаковых приоритетов
    
    def enqueue(self, item: Any, priority: int = 0):
        heapq.heappush(self.heap, (priority, self.counter, item))
        self.counter += 1
    
    def dequeue(self) -> Any:
        if self.is_empty():
            raise IndexError("Priority queue is empty")
        return heapq.heappop(self.heap)[2]
    
    def is_empty(self) -> bool:
        return len(self.heap) == 0
    
    def size(self) -> int:
        return len(self.heap)
    
    def __str__(self):
        return str([item for _, _, item in sorted(self.heap)])

# Демонстрация работы
if __name__ == "__main__":
    print("=== Python Demo ===")
    
    # Мультисписок
    ml = MultiList()
    ml.add_list([1, 2, 3])
    ml.add_list(['a', 'b', 'c'])
    print(f"MultiList: {ml}")
    print(f"All elements: {ml.get_all_elements()}")
    
    # Очередь
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print(f"\nQueue: {q}")
    print(f"Dequeue: {q.dequeue()}")
    print(f"Queue after dequeue: {q}")
    
    # Дек
    dq = Deque()
    dq.add_front(1)
    dq.add_rear(2)
    dq.add_front(0)
    print(f"\nDeque: {dq}")
    print(f"Remove front: {dq.remove_front()}")
    print(f"Remove rear: {dq.remove_rear()}")
    
    # Приоритетная очередь
    pq = PriorityQueue()
    pq.enqueue("Task 1", 2)
    pq.enqueue("Task 2", 1)
    pq.enqueue("Task 3", 3)
    print(f"\nPriorityQueue: {pq}")
    print(f"Dequeue: {pq.dequeue()}")
    print(f"Dequeue: {pq.dequeue()}")
