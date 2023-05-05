package programmers.problems.신규아이디추천;

/*
 * 내 풀이 : 하라는대로 단계적으로 수행하기
 */
public class Solution0 {
    public String solution(String new_id) {
        // 1단계
        String s1 = new_id.toLowerCase();
        
        // 2단계
        StringBuilder sb2 = new StringBuilder();
        for (char c : s1.toCharArray()){
            if (('a' <= c && c <= 'z') || ('0' <= c && c <= '9') || c == '-' || c == '_' || c == '.') 
                sb2.append(c);
        }
        
        // 3단계
        StringBuilder sb3 = new StringBuilder();
        for (char c : sb2.toString().toCharArray()){
            if (sb3.length() > 0 && sb3.charAt(sb3.length() - 1) == '.' && c == '.') continue;
            sb3.append(c);
        }
        
        // 4단계
        int firstIdx = (sb3.charAt(0) == '.') ? 1 : 0;
        int lastIdx = (sb3.length() > 1 && sb3.charAt(sb3.length() - 1) == '.') ? sb3.length() - 1 : sb3.length();
        String s4 = sb3.toString().substring(firstIdx, lastIdx);
        
        // 5단계
        String s5 = s4.equals("") ? "a" : s4;
        
        // 6단계
        String s6 = s5.length() > 15 ? s5.substring(0, 15) : s5;
        if (s6.charAt(s6.length() - 1) == '.') s6 = s6.substring(0, s6.length() - 1);
        
        // 7단계
        StringBuilder sb7 = new StringBuilder(s6);
        char lastChar = sb7.charAt(sb7.length() - 1);
        while (sb7.length() < 3){
            sb7.append(lastChar);
        }
        
        return sb7.toString();
    }
}
