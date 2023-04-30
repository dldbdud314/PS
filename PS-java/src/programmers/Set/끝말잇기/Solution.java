package programmers.Set.끝말잇기;

import java.util.*;

public class Solution {
    public boolean solution(String[] words) {
        Set<String> wSet = new HashSet<>();
        char last = words[0].charAt(0);
        for(String word : words){
            if (wSet.contains(word) || word.charAt(0) != last)
                return false;
            wSet.add(word);
            last = word.charAt(word.length() - 1);
        }
        return true;
    }
}
