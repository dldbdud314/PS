package programmers.Tree.더맵게;

import java.util.*;

class Solution {
    public int solution(int[] scoville, int K) {
        PriorityQueue<Integer> heap = new PriorityQueue<>();
        for (int x : scoville) heap.add(x);
        
        int cnt = 0;
        while (!heap.isEmpty()){
            if (heap.peek() >= K) return cnt;
            if (heap.size() == 1 && heap.peek() < K) return -1;
            
            int first = heap.poll();
            int sec = heap.isEmpty() ? 0 : heap.poll();
            
            heap.offer(first + sec * 2);
            
            cnt++;
        }
        
        return -1;
    }
}