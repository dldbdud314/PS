package programmers.Stack_Queue.기능개발;

import java.util.*;

// Queue 활용
public class Solution2 {
    public int[] solution(int[] progresses, int[] speeds) {
        Queue<Integer> days = new LinkedList<>();
        for (int i = 0; i < progresses.length; i++){
            days.offer((int)Math.ceil((100.0 - progresses[i])/speeds[i]));
        }
        
        List<Integer> res = new ArrayList<>();
        while (!days.isEmpty()){
            int day = days.poll();
            
            int cnt = 1;
            while (!days.isEmpty() && days.peek() <= day){
                days.poll();
                cnt++;
            }
            res.add(cnt);
        }
        
        return res.stream().mapToInt(Integer::intValue).toArray();
    }
    
}
