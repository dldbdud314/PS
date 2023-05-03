package programmers.Tree;

import java.util.*;

class MyData implements Comparable<MyData>{
    int v;

    MyData(int v){ this.v = v; }

    @Override
    public int compareTo(MyData o) {
        return Integer.compare(this.v, o.v);
    }

    @Override
    public String toString() {
        return Integer.toString(v);
    }
}

public class Main{
    public static void main(String[] args) {
        Set<MyData> set = new TreeSet<>();  // Binary Search Tree로 구현

        set.add(new MyData(1));
        set.add(new MyData(2));
        set.add(new MyData(3));
        
        System.out.println(set);

        // Min Heap / Max Heap -> new PriorityQueue<>)Comparator.reverseOrder())
        PriorityQueue<Integer> minHeap = new PriorityQueue<>(Comparator.reverseOrder());

        minHeap.offer(100);
        minHeap.offer(30);
        minHeap.offer(60);
        minHeap.offer(80);
        
        while(!minHeap.isEmpty()) System.out.println(minHeap.poll());

        PriorityQueue<Integer> queue = new PriorityQueue<>();

        Random r = new Random();
        for (int i = 0; i < 20; i++) queue.offer(r.nextInt(50));

        List<Integer> sorted = new LinkedList<>();
        while(!queue.isEmpty()) sorted.add(queue.poll());

        System.out.println(sorted);
    }
}