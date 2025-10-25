import java.util.*;

// 1. Мультисписок
class MultiList<T> {
    private List<List<T>> lists;
    
    public MultiList() {
        lists = new ArrayList<>();
    }
    
    public void addList(List<T> list) {
        lists.add(new ArrayList<>(list));
    }
    
    public List<T> getAllElements() {
        List<T> result = new ArrayList<>();
        for (List<T> list : lists) {
            result.addAll(list);
        }
        return result;
    }
    
    @Override
    public String toString() {
        return lists.toString();
    }
}

// 2. Очередь
class Queue<T> {
    private LinkedList<T> queue;
    
    public Queue() {
        queue = new LinkedList<>();
    }
    
    public void enqueue(T item) {
        queue.addLast(item);
    }
    
    public T dequeue() {
        if (isEmpty()) {
            throw new NoSuchElementException("Queue is empty");
        }
        return queue.removeFirst();
    }
    
    public boolean isEmpty() {
        return queue.isEmpty();
    }
    
    public int size() {
        return queue.size();
    }
    
    @Override
    public String toString() {
        return queue.toString();
    }
}

// 3. Дек
class Deque<T> {
    private LinkedList<T> deque;
    
    public Deque() {
        deque = new LinkedList<>();
    }
    
    public void addFront(T item) {
        deque.addFirst(item);
    }
    
    public void addRear(T item) {
        deque.addLast(item);
    }
    
    public T removeFront() {
        if (isEmpty()) {
            throw new NoSuchElementException("Deque is empty");
        }
        return deque.removeFirst();
    }
    
    public T removeRear() {
        if (isEmpty()) {
            throw new NoSuchElementException("Deque is empty");
        }
        return deque.removeLast();
    }
    
    public boolean isEmpty() {
        return deque.isEmpty();
    }
    
    public int size() {
        return deque.size();
    }
    
    @Override
    public String toString() {
        return deque.toString();
    }
}

// 4. Приоритетная очередь
class PriorityQueue<T> {
    private class Item implements Comparable<Item> {
        T value;
        int priority;
        long counter;
        
        Item(T value, int priority, long counter) {
            this.value = value;
            this.priority = priority;
            this.counter = counter;
        }
        
        @Override
        public int compareTo(Item other) {
            if (priority != other.priority) {
                return Integer.compare(priority, other.priority);
            }
            return Long.compare(counter, other.counter);
        }
    }
    
    private java.util.PriorityQueue<Item> heap;
    private long counter;
    
    public PriorityQueue() {
        heap = new java.util.PriorityQueue<>();
        counter = 0;
    }
    
    public void enqueue(T item, int priority) {
        heap.offer(new Item(item, priority, counter++));
    }
    
    public void enqueue(T item) {
        enqueue(item, 0);
    }
    
    public T dequeue() {
        if (isEmpty()) {
            throw new NoSuchElementException("Priority queue is empty");
        }
        return heap.poll().value;
    }
    
    public boolean isEmpty() {
        return heap.isEmpty();
    }
    
    public int size() {
        return heap.size();
    }
    
    @Override
    public String toString() {
        List<T> items = new ArrayList<>();
        for (Item item : heap) {
            items.add(item.value);
        }
        Collections.sort(items, (a, b) -> {
            // Для демонстрации, в реальности нужно сохранять порядок
            return a.toString().compareTo(b.toString());
        });
        return items.toString();
    }
}

// Демонстрация работы
public class DataStructuresDemo {
    public static void main(String[] args) {
        System.out.println("=== Java Demo ===");
        
        // Мультисписок
        MultiList<Integer> ml = new MultiList<>();
        ml.addList(Arrays.asList(1, 2, 3));
        ml.addList(Arrays.asList(4, 5, 6));
        System.out.println("MultiList: " + ml);
        System.out.println("All elements: " + ml.getAllElements());
        
        // Очередь
        Queue<Integer> q = new Queue<>();
        q.enqueue(1);
        q.enqueue(2);
        q.enqueue(3);
        System.out.println("\nQueue: " + q);
        System.out.println("Dequeue: " + q.dequeue());
        System.out.println("Queue after dequeue: " + q);
        
        // Дек
        Deque<Integer> dq = new Deque<>();
        dq.addFront(1);
        dq.addRear(2);
        dq.addFront(0);
        System.out.println("\nDeque: " + dq);
        System.out.println("Remove front: " + dq.removeFront());
        System.out.println("Remove rear: " + dq.removeRear());
        
        // Приоритетная очередь
        PriorityQueue<String> pq = new PriorityQueue<>();
        pq.enqueue("Task 1", 2);
        pq.enqueue("Task 2", 1);
        pq.enqueue("Task 3", 3);
        System.out.println("\nPriorityQueue: " + pq);
        System.out.println("Dequeue: " + pq.dequeue());
        System.out.println("Dequeue: " + pq.dequeue());
    }
}
