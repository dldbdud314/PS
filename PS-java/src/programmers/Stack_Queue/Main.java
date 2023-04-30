package programmers.Stack_Queue;

import java.util.*;

public class Main {
    public static void main(String[] args) {
        // Queue : 인터페이스만 제공
        Queue<Integer> queue = new LinkedList<>();

        queue.offer(1);
        queue.offer(2);
        queue.offer(3);
        queue.offer(4);

        queue.poll();
        System.out.println(queue);

        queue.poll();
        System.out.println(queue);

        System.out.println(queue.peek());

        // Stack -> Stack 클래스 제공
        Stack<Integer> stack = new Stack<>();

        stack.push(1);
        stack.push(3);
        stack.push(3);
        stack.push(5);

        System.out.println(stack);

        stack.pop();
        System.out.println(stack);

        System.out.println(stack.peek());

        // Deque : 양방향 넣고 빼기 -> offerFirst, offerLast, pollFirst, pollLast
        Deque<Integer> deque = new LinkedList<>();

        deque.offerFirst(1);
        deque.offerLast(2);
        deque.offerFirst(3);

        System.out.println(deque);
        System.out.println(deque.peekFirst());
        
        deque.pollFirst();
        System.out.println(deque);
    }
}