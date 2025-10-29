#include <iostream>
#include <vector>
#include <list>
#include <algorithm>
#include <climits>

// 1. Бинарная куча
class BinaryHeap {
private:
    std::vector<int> heap;

    int parent(int i) { return (i - 1) / 2; }
    int leftChild(int i) { return 2 * i + 1; }
    int rightChild(int i) { return 2 * i + 2; }

    void siftUp(int i) {
        while (i > 0 && heap[parent(i)] > heap[i]) {
            std::swap(heap[i], heap[parent(i)]);
            i = parent(i);
        }
    }

    void siftDown(int i) {
        int minIndex = i;
        int left = leftChild(i);
        int right = rightChild(i);

        if (left < heap.size() && heap[left] < heap[minIndex])
            minIndex = left;
        if (right < heap.size() && heap[right] < heap[minIndex])
            minIndex = right;

        if (i != minIndex) {
            std::swap(heap[i], heap[minIndex]);
            siftDown(minIndex);
        }
    }

public:
    void insert(int key) {
        heap.push_back(key);
        siftUp(heap.size() - 1);
    }

    int extractMin() {
        if (heap.empty()) return -1;
        
        int result = heap[0];
        heap[0] = heap.back();
        heap.pop_back();
        
        if (!heap.empty()) siftDown(0);
        return result;
    }

    void print() {
        std::cout << "Binary Heap: ";
        for (int val : heap) std::cout << val << " ";
        std::cout << std::endl;
    }
};

// 2. Биномиальная куча (упрощенная реализация)
struct BinomialNode {
    int key;
    int degree;
    BinomialNode* child;
    BinomialNode* sibling;
    
    BinomialNode(int k) : key(k), degree(0), child(nullptr), sibling(nullptr) {}
};

class BinomialHeap {
private:
    BinomialNode* head;

    BinomialNode* mergeTrees(BinomialNode* t1, BinomialNode* t2) {
        if (t1->key > t2->key) std::swap(t1, t2);
        t2->sibling = t1->child;
        t1->child = t2;
        t1->degree++;
        return t1;
    }

public:
    BinomialHeap() : head(nullptr) {}
    
    void insert(int key) {
        BinomialHeap tempHeap;
        tempHeap.head = new BinomialNode(key);
        merge(tempHeap);
    }
    
    void merge(BinomialHeap& other) {
        // Реализация объединения куч
    }
};

// 3. Хеш-таблица с цепочками
class HashTable {
private:
    int size;
    std::vector<std::list<std::pair<int, int>>> table;

    int hash(int key) {
        return key % size;
    }

public:
    HashTable(int s = 10) : size(s), table(s) {}

    void insert(int key, int value) {
        int index = hash(key);
        for (auto& pair : table[index]) {
            if (pair.first == key) {
                pair.second = value;
                return;
            }
        }
        table[index].push_back({key, value});
    }

    int get(int key) {
        int index = hash(key);
        for (auto& pair : table[index]) {
            if (pair.first == key) {
                return pair.second;
            }
        }
        return -1;
    }

    void remove(int key) {
        int index = hash(key);
        table[index].remove_if([key](auto pair) { return pair.first == key; });
    }

    void print() {
        std::cout << "Hash Table:" << std::endl;
        for (int i = 0; i < size; i++) {
            std::cout << i << ": ";
            for (auto& pair : table[i]) {
                std::cout << "(" << pair.first << "," << pair.second << ") ";
            }
            std::cout << std::endl;
        }
    }
};

int main() {
    std::cout << "=== C++ Demo ===" << std::endl;
    
    // Бинарная куча
    BinaryHeap bh;
    bh.insert(5);
    bh.insert(3);
    bh.insert(8);
    bh.insert(1);
    bh.insert(2);
    bh.print();
    std::cout << "Extract min: " << bh.extractMin() << std::endl;
    
    // Хеш-таблица
    HashTable ht;
    ht.insert(1, 100);
    ht.insert(2, 200);
    ht.insert(11, 300); // Коллизия с 1
    ht.print();
    
    return 0;
}
