package programmers.Set.같은숫자는싫어;

import java.util.*;

public class Solution {
    public int[] solution(int []arr) {
        List<Integer> lst = new ArrayList<>();
        
        int prev = -1;
        for(int x : arr){
            if (x != prev){
                lst.add(x);
                prev = x;
            }
        }
        
        return lst.stream()
            .mapToInt(Integer::intValue)
            .toArray();
    }
}
