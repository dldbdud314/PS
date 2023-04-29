package programmers.Map.위장;

import java.util.*;

public class Solution {
    public int solution(String[][] clothes) {
        Map<String, Integer> clothesMap = new HashMap<>();
        for (String[] cloth : clothes){
            Integer count = clothesMap.getOrDefault(cloth[1], 0);
            clothesMap.put(cloth[1], count + 1);
        }

        int total = 1;
        for (Integer count : clothesMap.values()){
            total *= (count + 1);
        }
        return total - 1;
    }
}
