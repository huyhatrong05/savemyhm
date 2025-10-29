#include <iostream>
#include <vector>
#include <queue>
#include <unordered_map>
#include <unordered_set>
#include <stack>
#include <climits>
#include <algorithm>

// 1. Узел бинарного дерева
struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

class BinaryTree {
private:
    TreeNode* root;

    TreeNode* insertRecursive(TreeNode* node, int val) {
        if (!node) return new TreeNode(val);
        
        if (val < node->val) {
            node->left = insertRecursive(node->left, val);
        } else {
            node->right = insertRecursive(node->right, val);
        }
        return node;
    }

    void inorderRecursive(TreeNode* node) {
        if (node) {
            inorderRecursive(node->left);
            std::cout << node->val << " ";
            inorderRecursive(node->right);
        }
    }

public:
    BinaryTree() : root(nullptr) {}
    
    void insert(int val) {
        root = insertRecursive(root, val);
    }
    
    void inorder() {
        std::cout << "Inorder: ";
        inorderRecursive(root);
        std::cout << std::endl;
    }
    
    std::vector<std::vector<int>> levelOrder() {
        std::vector<std::vector<int>> result;
        if (!root) return result;
        
        std::queue<TreeNode*> q;
        q.push(root);
        
        while (!q.empty()) {
            int levelSize = q.size();
            std::vector<int> level;
            
            for (int i = 0; i < levelSize; i++) {
                TreeNode* node = q.front();
                q.pop();
                level.push_back(node->val);
                
                if (node->left) q.push(node->left);
                if (node->right) q.push(node->right);
            }
            result.push_back(level);
        }
        return result;
    }
};

// 2. Граф (список смежности)
class Graph {
private:
    std::unordered_map<int, std::vector<std::pair<int, int>>> adjList;
    bool directed;

public:
    Graph(bool dir = false) : directed(dir) {}
    
    void addEdge(int u, int v, int weight = 1) {
        adjList[u].push_back({v, weight});
        if (!directed) {
            adjList[v].push_back({u, weight});
        }
    }
    
    std::vector<int> bfs(int start) {
        std::vector<int> result;
        std::unordered_set<int> visited;
        std::queue<int> q;
        
        q.push(start);
        visited.insert(start);
        
        while (!q.empty()) {
            int vertex = q.front();
            q.pop();
            result.push_back(vertex);
            
            for (auto& neighbor : adjList[vertex]) {
                if (visited.find(neighbor.first) == visited.end()) {
                    visited.insert(neighbor.first);
                    q.push(neighbor.first);
                }
            }
        }
        return result;
    }
    
    std::vector<int> dfs(int start) {
        std::vector<int> result;
        std::unordered_set<int> visited;
        std::stack<int> st;
        
        st.push(start);
        visited.insert(start);
        
        while (!st.empty()) {
            int vertex = st.top();
            st.pop();
            result.push_back(vertex);
            
            for (auto& neighbor : adjList[vertex]) {
                if (visited.find(neighbor.first) == visited.end()) {
                    visited.insert(neighbor.first);
                    st.push(neighbor.first);
                }
            }
        }
        return result;
    }
    
    std::unordered_map<int, int> dijkstra(int start) {
        std::unordered_map<int, int> distances;
        for (auto& vertex : adjList) {
            distances[vertex.first] = INT_MAX;
        }
        distances[start] = 0;
        
        using Pair = std::pair<int, int>;
        std::priority_queue<Pair, std::vector<Pair>, std::greater<Pair>> pq;
        pq.push({0, start});
        
        while (!pq.empty()) {
            int currentDist = pq.top().first;
            int currentVertex = pq.top().second;
            pq.pop();
            
            if (currentDist > distances[currentVertex]) {
                continue;
            }
            
            for (auto& neighbor : adjList[currentVertex]) {
                int nextVertex = neighbor.first;
                int weight = neighbor.second;
                int distance = currentDist + weight;
                
                if (distance < distances[nextVertex]) {
                    distances[nextVertex] = distance;
                    pq.push({distance, nextVertex});
                }
            }
        }
        return distances;
    }
};

int main() {
    std::cout << "=== C++ Demo ===" << std::endl;
    
    // Бинарное дерево
    BinaryTree bt;
    std::vector<int> values = {5, 3, 7, 2, 4, 6, 8};
    for (int val : values) {
        bt.insert(val);
    }
    
    bt.inorder();
    auto levels = bt.levelOrder();
    std::cout << "Level order: ";
    for (auto& level : levels) {
        for (int val : level) {
            std::cout << val << " ";
        }
    }
    std::cout << std::endl;
    
    // Граф
    Graph g;
    g.addEdge(0, 1);
    g.addEdge(0, 2);
    g.addEdge(1, 3);
    g.addEdge(2, 4);
    g.addEdge(3, 5);
    
    auto bfsResult = g.bfs(0);
    std::cout << "BFS from 0: ";
    for (int vertex : bfsResult) {
        std::cout << vertex << " ";
    }
    std::cout << std::endl;
    
    auto dfsResult = g.dfs(0);
    std::cout << "DFS from 0: ";
    for (int vertex : dfsResult) {
        std::cout << vertex << " ";
    }
    std::cout << std::endl;
    
    return 0;
}
