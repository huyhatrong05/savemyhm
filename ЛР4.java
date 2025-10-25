import java.util.*;

// 1. Узел бинарного дерева
class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    
    TreeNode(int val) {
        this.val = val;
    }
}

class BinaryTree {
    private TreeNode root;
    
    public void insert(int val) {
        root = insertRecursive(root, val);
    }
    
    private TreeNode insertRecursive(TreeNode node, int val) {
        if (node == null) {
            return new TreeNode(val);
        }
        
        if (val < node.val) {
            node.left = insertRecursive(node.left, val);
        } else {
            node.right = insertRecursive(node.right, val);
        }
        return node;
    }
    
    public void inorder() {
        System.out.print("Inorder: ");
        inorderRecursive(root);
        System.out.println();
    }
    
    private void inorderRecursive(TreeNode node) {
        if (node != null) {
            inorderRecursive(node.left);
            System.out.print(node.val + " ");
            inorderRecursive(node.right);
        }
    }
    
    public List<List<Integer>> levelOrder() {
        List<List<Integer>> result = new ArrayList<>();
        if (root == null) return result;
        
        Queue<TreeNode> queue = new LinkedList<>();
        queue.offer(root);
        
        while (!queue.isEmpty()) {
            int levelSize = queue.size();
            List<Integer> level = new ArrayList<>();
            
            for (int i = 0; i < levelSize; i++) {
                TreeNode node = queue.poll();
                level.add(node.val);
                
                if (node.left != null) queue.offer(node.left);
                if (node.right != null) queue.offer(node.right);
            }
            result.add(level);
        }
        return result;
    }
}

// 2. Граф
class Graph {
    private Map<Integer, List<Pair>> adjList;
    private boolean directed;
    
    private class Pair {
        int vertex;
        int weight;
        
        Pair(int vertex, int weight) {
            this.vertex = vertex;
            this.weight = weight;
        }
    }
    
    public Graph(boolean directed) {
        this.adjList = new HashMap<>();
        this.directed = directed;
    }
    
    public Graph() {
        this(false);
    }
    
    public void addEdge(int u, int v, int weight) {
        adjList.putIfAbsent(u, new ArrayList<>());
        adjList.putIfAbsent(v, new ArrayList<>());
        
        adjList.get(u).add(new Pair(v, weight));
        if (!directed) {
            adjList.get(v).add(new Pair(u, weight));
        }
    }
    
    public void addEdge(int u, int v) {
        addEdge(u, v, 1);
    }
    
    public List<Integer> bfs(int start) {
        List<Integer> result = new ArrayList<>();
        Set<Integer> visited = new HashSet<>();
        Queue<Integer> queue = new LinkedList<>();
        
        queue.offer(start);
        visited.add(start);
        
        while (!queue.isEmpty()) {
            int vertex = queue.poll();
            result.add(vertex);
            
            if (adjList.containsKey(vertex)) {
                for (Pair neighbor : adjList.get(vertex)) {
                    if (!visited.contains(neighbor.vertex)) {
                        visited.add(neighbor.vertex);
                        queue.offer(neighbor.vertex);
                    }
                }
            }
        }
        return result;
    }
    
    public List<Integer> dfs(int start) {
        List<Integer> result = new ArrayList<>();
        Set<Integer> visited = new HashSet<>();
        Stack<Integer> stack = new Stack<>();
        
        stack.push(start);
        visited.add(start);
        
        while (!stack.isEmpty()) {
            int vertex = stack.pop();
            result.add(vertex);
            
            if (adjList.containsKey(vertex)) {
                for (Pair neighbor : adjList.get(vertex)) {
                    if (!visited.contains(neighbor.vertex)) {
                        visited.add(neighbor.vertex);
                        stack.push(neighbor.vertex);
                    }
                }
            }
        }
        return result;
    }
    
    public Map<Integer, Integer> dijkstra(int start) {
        Map<Integer, Integer> distances = new HashMap<>();
        for (Integer vertex : adjList.keySet()) {
            distances.put(vertex, Integer.MAX_VALUE);
        }
        distances.put(start, 0);
        
        PriorityQueue<Pair> pq = new PriorityQueue<>(
            Comparator.comparingInt(a -> a.weight)
        );
        pq.offer(new Pair(start, 0));
        
        while (!pq.isEmpty()) {
            Pair current = pq.poll();
            int currentVertex = current.vertex;
            int currentDist = current.weight;
            
            if (currentDist > distances.get(currentVertex)) {
                continue;
            }
            
            if (adjList.containsKey(currentVertex)) {
                for (Pair neighbor : adjList.get(currentVertex)) {
                    int distance = currentDist + neighbor.weight;
                    
                    if (distance < distances.get(neighbor.vertex)) {
                        distances.put(neighbor.vertex, distance);
                        pq.offer(new Pair(neighbor.vertex, distance));
                    }
                }
            }
        }
        return distances;
    }
}

// Демонстрация
public class TreeGraphDemo {
    public static void main(String[] args) {
        System.out.println("=== Java Demo ===");
        
        // Бинарное дерево
        BinaryTree bt = new BinaryTree();
        int[] values = {5, 3, 7, 2, 4, 6, 8};
        for (int val : values) {
            bt.insert(val);
        }
        
        bt.inorder();
        List<List<Integer>> levels = bt.levelOrder();
        System.out.println("Level order: " + levels);
        
        // Граф
        Graph g = new Graph();
        g.addEdge(0, 1);
        g.addEdge(0, 2);
        g.addEdge(1, 3);
        g.addEdge(2, 4);
        g.addEdge(3, 5);
        
        System.out.println("BFS from 0: " + g.bfs(0));
        System.out.println("DFS from 0: " + g.dfs(0));
        
        // Взвешенный граф
        Graph weightedG = new Graph();
        weightedG.addEdge(0, 1, 4);
        weightedG.addEdge(0, 2, 1);
        weightedG.addEdge(2, 1, 2);
        weightedG.addEdge(1, 3, 1);
        weightedG.addEdge(2, 3, 5);
        
        System.out.println("Dijkstra from 0: " + weightedG.dijkstra(0));
    }
}
