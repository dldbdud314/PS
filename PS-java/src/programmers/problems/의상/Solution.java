package programmers.problems.의상;

import java.util.*;

class Solution {
    public int solution(String[][] clothes) {
        // 맵에 담기
        Map<String, List<String>> map = new HashMap<>();
        for (String[] x : clothes){
            List<String> cList = new ArrayList<>();
            if (map.containsKey(x[1])) cList = map.get(x[1]);
            cList.add(x[0]);
            map.put(x[1], cList);
        }
        
        // 조합의 수 구하기
        int total = 1;
        for (String key : map.keySet()){
            total *= (map.get(key).size() + 1);
        }
        return total - 1;
    }
}