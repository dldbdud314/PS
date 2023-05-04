package programmers.Stack_Queue.기능개발;

import java.util.*;

// 단순 리스트 활용
class Solution1 {
    public int[] solution(int[] progresses, int[] speeds) {
        List<Integer> cnts = new ArrayList<>();
        List<Integer> time = new ArrayList<>();
        int biggest = 0;
        for (int i = 0; i < speeds.length; i++){
            int p = progresses[i], s = speeds[i];
            int t = (int)Math.ceil((100.0 - p) / s);
            
            if (i == 0){
                biggest = t;
            }
            else if (!time.isEmpty() && biggest < t){
                cnts.add(time.size());
                time.clear();
                
                biggest = t;
            }
            time.add(t);
        }
        if (!time.isEmpty()) cnts.add(time.size());
        
        return cnts.stream().mapToInt(Integer::intValue).toArray();
    }
}
