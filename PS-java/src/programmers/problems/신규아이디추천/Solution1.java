package programmers.problems.신규아이디추천;

/*
 * Regex 활용하기
 */
public class Solution1 {
    public String solution(String new_id) {
        // 1단계
        String s1 = new_id.toLowerCase();

        // 2단계
        String s2 = s1.replaceAll("[^-_.a-z0-9]", "");

        // 3단계
        String s3 = s2.replaceAll("[.]{2,}", ".");

        // 4단계
        String s4 = s3.replaceAll("^[.]|[.]$", "");

        // 5단계
        String s5 = s4.equals("") ? "a" : s4;

        // 6단계
        String s6 = s5;
        if (s6.length() >= 16){
            s6 = s5.substring(0, 15).replaceAll("[.]$", "");
        }

        // 7단계
        StringBuilder sb7 = new StringBuilder(s6);
        char lastChar = sb7.charAt(sb7.length() - 1);
        while (sb7.length() < 3){
            sb7.append(lastChar);
        }

        return sb7.toString();
    }
}
