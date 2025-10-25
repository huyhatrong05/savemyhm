from collections import deque, defaultdict
import heapq

# 1. Бинарное дерево
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self):
        self.root = None
    
    def insert(self, val):
        if not self.root:
            self.root = TreeNode(val)
        else:
            self._insert_recursive(self.root, val)
    
    def _insert_recursive(self, node, val):
        if val < node.val:
            if node.left:
                self._insert_recursive(node.left, val)
            else:
                node.left = TreeNode(val)
        else:
            if node.right:
                self._insert_recursive(node.right, val)
            else:
                node.right = TreeNode(val)
    
    def inorder_traversal(self, node):
        if node:
            self.inorder_traversal(node.left)
            print(node.val, end=" ")
            self.inorder_traversal(node.right)
    
    def level_order_traversal(self):
        if not self.root:
            return []
        
        result = []
        queue = deque([self.root])
        
        while queue:
            level_size = len(queue)
            level = []
            
            for _ in range(level_size):
                node = queue.popleft()
                level.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            result.append(level)
        return result

# 2. Двоичное дерево поиска (BST)
class BST:
    def __init__(self):
        self.root = None
    
    def insert(self, val):
        self.root = self._insert(self.root, val)
    
    def _insert(self, node, val):
        if not node:
            return TreeNode(val)
        
        if val < node.val:
            node.left = self._insert(node.left, val)
        else:
            node.right = self._insert(node.right, val)
        
        return node
    
    def search(self, val):
        return self._search(self.root, val)
    
    def _search(self, node, val):
        if not node or node.val == val:
            return node
        
        if val < node.val:
            return self._search(node.left, val)
        return self._search(node.right, val)

# 3. Граф (список смежности)
class Graph:
    def __init__(self, directed=False):
        self.graph = defaultdict(list)
        self.directed = directed
    
    def add_edge(self, u, v, weight=1):
        self.graph[u].append((v, weight))
        if not self.directed:
            self.graph[v].append((u, weight))
    
    def bfs(self, start):
        visited = set()
        queue = deque([start])
        visited.add(start)
        result = []
        
        while queue:
            vertex = queue.popleft()
            result.append(vertex)
            
            for neighbor, _ in self.graph[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        
        return result
    
    def dfs(self, start):
        visited = set()
        result = []
        self._dfs_recursive(start, visited, result)
        return result
    
    def _dfs_recursive(self, vertex, visited, result):
        visited.add(vertex)
        result.append(vertex)
        
        for neighbor, _ in self.graph[vertex]:
            if neighbor not in visited:
                self._dfs_recursive(neighbor, visited, result)
    
    def dijkstra(self, start):
        distances = {vertex: float('inf') for vertex in self.graph}
        distances[start] = 0
        pq = [(0, start)]
        
        while pq:
            current_dist, current_vertex = heapq.heappop(pq)
            
            if current_dist > distances[current_vertex]:
                continue
            
            for neighbor, weight in self.graph[current_vertex]:
                distance = current_dist + weight
                
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(pq, (distance, neighbor))
        
        return distances

# Демонстрация
if __name__ == "__main__":
    print("=== Python Demo ===")
    
    # Бинарное дерево
    bt = BinaryTree()
    for val in [5, 3, 7, 2, 4, 6, 8]:
        bt.insert(val)
    
    print("Inorder traversal:", end=" ")
    bt.inorder_traversal(bt.root)
    print("\nLevel order traversal:", bt.level_order_traversal())
    
    # Граф
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 4)
    g.add_edge(3, 5)
    
    print("BFS from 0:", g.bfs(0))
    print("DFS from 0:", g.dfs(0))
    
    # Взвешенный граф для Дейкстры
    weighted_g = Graph()
    weighted_g.add_edge(0, 1, 4)
    weighted_g.add_edge(0, 2, 1)
    weighted_g.add_edge(2, 1, 2)
    weighted_g.add_edge(1, 3, 1)
    weighted_g.add_edge(2, 3, 5)
    
    print("Dijkstra from 0:", weighted_g.dijkstra(0))
