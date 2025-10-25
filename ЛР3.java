import java.util.*;

// 1. Бинарная куча
class BinaryHeap {
    private List<Integer> heap;
    
    public BinaryHeap() {
        heap = new ArrayList<>();
    }
    
    private int parent(int i) { return (i - 1) / 2; }
    private int leftChild(int i) { return 2 * i + 1; }
    private int rightChild(int i) { return 2 * i + 2; }
    
    public void insert(int key) {
        heap.add(key);
        siftUp(heap.size() - 1);
    }
    
    public Integer extractMin() {
        if (heap.isEmpty()) return null;
        
        int min = heap.get(0);
        heap.set(0, heap.get(heap.size() - 1));
        heap.remove(heap.size() - 1);
        
        if (!heap.isEmpty()) siftDown(0);
        return min;
    }
    
    private void siftUp(int i) {
        while (i > 0 && heap.get(parent(i)) > heap.get(i)) {
            Collections.swap(heap, i, parent(i));
            i = parent(i);
        }
    }
    
    private void siftDown(int i) {
        int minIndex = i;
        int left = leftChild(i);
        int right = rightChild(i);
        
        if (left < heap.size() && heap.get(left) < heap.get(minIndex)) {
            minIndex = left;
        }
        if (right < heap.size() && heap.get(right) < heap.get(minIndex)) {
            minIndex = right;
        }
        
        if (i != minIndex) {
            Collections.swap(heap, i, minIndex);
            siftDown(minIndex);
        }
    }
    
    @Override
    public String toString() {
        return "BinaryHeap: " + heap.toString();
    }
}

// 2. Биномиальная куча (базовая структура)
class BinomialNode {
    int key;
    int degree;
    BinomialNode child;
    BinomialNode sibling;
    
    public BinomialNode(int key) {
        this.key = key;
        this.degree = 0;
    }
}

class BinomialHeap {
    private BinomialNode head;
    
    public BinomialHeap() {
        head = null;
    }
    
    public void insert(int key) {
        BinomialHeap tempHeap = new BinomialHeap();
        tempHeap.head = new BinomialNode(key);
        merge(tempHeap);
    }
    
    public void merge(BinomialHeap other) {
        // Реализация объединения
    }
}

// 3. Хеш-таблица
class HashTable<K, V> {
    private class Entry<K, V> {
        K key;
        V value;
        
        Entry(K key, V value) {
            this.key = key;
            this.value = value;
        }
    }
    
    private int size;
    private LinkedList<Entry<K, V>>[] table;
    
    @SuppressWarnings("unchecked")
    public HashTable(int size) {
        this.size = size;
        table = new LinkedList[size];
        for (int i = 0; i < size; i++) {
            table[i] = new LinkedList<>();
        }
    }
    
    private int hash(K key) {
        return Math.abs(key.hashCode()) % size;
    }
    
    public void put(K key, V value) {
        int index = hash(key);
        for (Entry<K, V> entry : table[index]) {
            if (entry.key.equals(key)) {
                entry.value = value;
                return;
            }
        }
        table[index].add(new Entry<>(key, value));
    }
    
    public V get(K key) {
        int index = hash(key);
        for (Entry<K, V> entry : table[index]) {
            if (entry.key.equals(key)) {
                return entry.value;
            }
        }
        return null;
    }
    
    public void remove(K key) {
        int index = hash(key);
        table[index].removeIf(entry -> entry.key.equals(key));
    }
    
    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < size; i++) {
            sb.append(i).append(": ");
            for (Entry<K, V> entry : table[i]) {
                sb.append("(").append(entry.key).append(",").append(entry.value).append(") ");
            }
            sb.append("\n");
        }
        return sb.toString();
    }
}

// Демонстрация
public class HeapDemo {
    public static void main(String[] args) {
        System.out.println("=== Java Demo ===");
        
        // Бинарная куча
        BinaryHeap bh = new BinaryHeap();
        bh.insert(5);
        bh.insert(3);
        bh.insert(8);
        bh.insert(1);
        bh.insert(2);
        System.out.println(bh);
        System.out.println("Extract min: " + bh.extractMin());
        
        // Хеш-таблица
        HashTable<String, Integer> ht = new HashTable<>(10);
        ht.put("apple", 10);
        ht.put("banana", 20);
        ht.put("orange", 30);
        System.out.println("HashTable get apple: " + ht.get("apple"));
        System.out.println(ht);
    }
}
