package programmers.선형탐색.스킬트리;

import java.util.*;

public class Solution2 {
    public int solution(String skill, String[] skill_trees) {
        int cnt = 0;
        for (String skill_tree : skill_trees) {
            String s2 = skill_tree.replaceAll("[^" + skill + "]", "");
            if (skill.startsWith(s2)) cnt++;
        }
        return cnt;
    }

    public int solution_toStream(String skill, String[] skill_trees) {
        return (int)Arrays.stream(skill_trees)
                .map(s -> s.replaceAll("[^" + skill + "]", ""))
                .filter(s -> skill.startsWith(s))
                .count();
    }
}
