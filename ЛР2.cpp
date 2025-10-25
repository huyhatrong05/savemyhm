#include <iostream>
#include <vector>
#include <deque>
#include <queue>
#include <list>
#include <string>

// 1. Мультисписок
template<typename T>
class MultiList {
private:
    std::vector<std::list<T>> lists;

public:
    void addList(const std::list<T>& lst) {
        lists.push_back(lst);
    }
    
    std::vector<T> getAllElements() const {
        std::vector<T> result;
        for (const auto& lst : lists) {
            for (const auto& item : lst) {
                result.push_back(item);
            }
        }
        return result;
    }
    
    void print() const {
        std::cout << "MultiList: ";
        for (size_t i = 0; i < lists.size(); ++i) {
            std::cout << "[";
            for (const auto& item : lists[i]) {
                std::cout << item << " ";
            }
            std::cout << "] ";
        }
        std::cout << std::endl;
    }
};

// 2. Очередь
template<typename T>
class Queue {
private:
    std::deque<T> queue;

public:
    void enqueue(const T& item) {
        queue.push_back(item);
    }
    
    T dequeue() {
        if (isEmpty()) {
            throw std::runtime_error("Queue is empty");
        }
        T item = queue.front();
        queue.pop_front();
        return item;
    }
    
    bool isEmpty() const {
        return queue.empty();
    }
    
    size_t size() const {
        return queue.size();
    }
    
    void print() const {
        std::cout << "Queue: ";
        for (const auto& item : queue) {
            std::cout << item << " ";
        }
        std::cout << std::endl;
    }
};

// 3. Дек
template<typename T>
class Deque {
private:
    std::deque<T> deque;

public:
    void addFront(const T& item) {
        deque.push_front(item);
    }
    
    void addRear(const T& item) {
        deque.push_back(item);
    }
    
    T removeFront() {
        if (isEmpty()) {
            throw std::runtime_error("Deque is empty");
        }
        T item = deque.front();
        deque.pop_front();
        return item;
    }
    
    T removeRear() {
        if (isEmpty()) {
            throw std::runtime_error("Deque is empty");
        }
        T item = deque.back();
        deque.pop_back();
        return item;
    }
    
    bool isEmpty() const {
        return deque.empty();
    }
    
    size_t size() const {
        return deque.size();
    }
    
    void print() const {
        std::cout << "Deque: ";
        for (const auto& item : deque) {
            std::cout << item << " ";
        }
        std::cout << std::endl;
    }
};

// 4. Приоритетная очередь
template<typename T>
class PriorityQueue {
private:
    struct Item {
        T value;
        int priority;
        
        bool operator<(const Item& other) const {
            return priority > other.priority; // min-heap
        }
    };
    
    std::priority_queue<Item> heap;

public:
    void enqueue(const T& item, int priority = 0) {
        heap.push({item, priority});
    }
    
    T dequeue() {
        if (isEmpty()) {
            throw std::runtime_error("Priority queue is empty");
        }
        T item = heap.top().value;
        heap.pop();
        return item;
    }
    
    bool isEmpty() const {
        return heap.empty();
    }
    
    size_t size() const {
        return heap.size();
    }
};

int main() {
    std::cout << "=== C++ Demo ===" << std::endl;
    
    // Мультисписок
    MultiList<int> ml;
    ml.addList({1, 2, 3});
    ml.addList({4, 5, 6});
    ml.print();
    
    // Очередь
    Queue<int> q;
    q.enqueue(1);
    q.enqueue(2);
    q.enqueue(3);
    q.print();
    std::cout << "Dequeue: " << q.dequeue() << std::endl;
    
    // Дек
    Deque<int> dq;
    dq.addFront(1);
    dq.addRear(2);
    dq.addFront(0);
    dq.print();
    std::cout << "Remove front: " << dq.removeFront() << std::endl;
    std::cout << "Remove rear: " << dq.removeRear() << std::endl;
    
    // Приоритетная очередь
    PriorityQueue<std::string> pq;
    pq.enqueue("Task 1", 2);
    pq.enqueue("Task 2", 1);
    pq.enqueue("Task 3", 3);
    std::cout << "PriorityQueue dequeue: " << pq.dequeue() << std::endl;
    std::cout << "PriorityQueue dequeue: " << pq.dequeue() << std::endl;
    
    return 0;
}
