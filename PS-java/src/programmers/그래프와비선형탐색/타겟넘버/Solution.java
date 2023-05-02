package programmers.그래프와비선형탐색.타겟넘버;

import java.util.*;

class Solution {
    public int solution(int[] numbers, int target) {
        Queue<Integer> queue = new LinkedList<>();
        queue.offer(0);
        
        for (int i = 0; i < numbers.length; i++){
            for (int j = 0; j < Math.pow(2, i); j++){
                int front = queue.poll();
                
                queue.offer(front - numbers[i]);
                queue.offer(front + numbers[i]);
            }
        }
        
        int cnt = 0;
        for (int number : queue){
            if (number == target) cnt++;
        }

        return cnt;
    }
}
