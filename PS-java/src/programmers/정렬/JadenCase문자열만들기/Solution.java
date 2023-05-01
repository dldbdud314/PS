package programmers.정렬.JadenCase문자열만들기;

public class Solution {
    public String solution(String s){
        StringBuilder res = new StringBuilder();
        String s2 = s.toLowerCase();
        char last = ' ';
        for (char c : s2.toCharArray()){
            if (last == ' ') c = Character.toUpperCase(c);
            res.append(c);
            last = c;
        }
        return res.toString();
    }
}
