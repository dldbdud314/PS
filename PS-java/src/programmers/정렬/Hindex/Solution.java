package programmers.정렬.Hindex;

import java.util.*;

public class Solution {
    public int solution(int[] citations) {
        int res = 0;
        Arrays.sort(citations);
        for (int i = 0; i < citations.length; i++){
            if (citations[i] >= citations.length - i){
                res = citations.length - i;
                break;
            }
        }
        return res;
    }
}
