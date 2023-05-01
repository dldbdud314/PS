package programmers.정렬.제일작은수제거하기;

import java.util.*;

public class Solution {
    public int[] solution(int[] arr) {
        int min = Arrays.stream(arr).min().getAsInt();
        
        List<Integer> res = new ArrayList<>();
        for (int x : arr){
            if (x == min) continue;
            res.add(x);
        }
        
        return (res.size() == 0) ? new int[]{-1} : res.stream().mapToInt(Integer::intValue).toArray();
    }
}
