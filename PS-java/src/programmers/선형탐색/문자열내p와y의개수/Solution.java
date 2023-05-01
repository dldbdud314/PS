package programmers.선형탐색.문자열내p와y의개수;

public class Solution {
    boolean solution0(String s) {
        int pCnt = 0, yCnt = 0;
        for (char c : s.toLowerCase().toCharArray()){
            if (c == 'p') pCnt++;
            if (c == 'y') yCnt++;
        }
        
        return pCnt == yCnt;
    }

    // regex 활용 -> pP/yY만 남기고 모두 제거
    boolean solution1(String s) {
        int pCnt = s.replaceAll("[^pP]", "").length();
        int yCnt = s.replaceAll("[^yY]", "").length();
        
        return pCnt == yCnt;
    }
}
