package programmers.problems.크기가작은부분문자열;

class Solution {
    public int solution(String t, String p) {
        long intP = Long.valueOf(p);
        int cnt = 0;
        for(int i = 0; i < t.length() - p.length() + 1; i++){
            String subStr = t.substring(i, i + p.length());
            if (Long.valueOf(subStr) <= intP) cnt++;
        }
        
        return cnt;
    }
}