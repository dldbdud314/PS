package programmers.problems.K번째수;

import java.util.*;

public class Solution {
    public int[] solution(int[] array, int[][] commands) {
        List<Integer> list = new ArrayList<>();
        for (int[] command : commands){
            int[] arrCp = Arrays.copyOfRange(array, command[0] - 1, command[1]);
            Arrays.sort(arrCp);
            
            list.add(arrCp[command[2] - 1]);
        }
        
        return list.stream()
            .mapToInt(Integer::intValue)
            .toArray();
    }
}
