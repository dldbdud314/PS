package programmers.problems.가장가까운같은글자;

import java.util.*;

class Solution {
    public int[] solution(String s) {
        Map<Character, Integer> map = new HashMap<>();
        int[] pos = new int[s.length()];
        Arrays.fill(pos, -1);
        for (int i = 0; i < s.length(); i++){
            char c = s.charAt(i);
            if (map.containsKey(c)) pos[i] = i - map.get(c);
            map.put(c, i);
        }
        
        return pos;
    }
}
