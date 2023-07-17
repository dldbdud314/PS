package programmers.problems.튜플;
/*
- s 파싱하고
- 길이 순으로 목록 sorting
- 다른 요소 하나씩 덧붙이기
*/

import java.util.*;

public class Solution {
    public ArrayList<Integer> solution(String s) {
        String[] ss = s.substring(2, s.length() - 2).split("\\},\\{");
        Arrays.sort(ss,
                (s1, s2) -> Integer.compare(s1.length(), s2.length()));

        Set<Integer> tSet = new HashSet<>();
        ArrayList<Integer> res = new ArrayList<>();
        for (String s1 : ss){
            for (String tmp : s1.split(",")){
                Integer n1 = Integer.parseInt(tmp);
                if (tSet.add(n1)) res.add(n1);
            }
        }
        return res;
    }
}
