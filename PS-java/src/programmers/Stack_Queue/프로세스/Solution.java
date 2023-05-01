package programmers.Stack_Queue.프로세스;

import java.util.*;

class Solution {
    public int solution(int[] priorities, int location) {
        Queue<Integer> queue = new LinkedList<>();
        for (int priority : priorities) {
            queue.add(priority);
        }
        
        int cnt = 1;
        while (!queue.isEmpty()){
            int front = queue.poll();
            
            boolean flag = true;
            for (int x: queue){
                if (x > front){
                    flag = false;
                    break;
                }
            }
            if (flag) {
                if (location == 0) break;
                cnt++;  // 큐에서 아예 뺀 경우에만 ++ 
            }
            else{
                queue.offer(front);
            }
            
            location--;
            if (location == -1) location = queue.size() - 1;
        }
        
        return cnt;
    }
}