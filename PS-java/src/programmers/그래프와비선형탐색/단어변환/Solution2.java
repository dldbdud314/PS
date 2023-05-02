package programmers.그래프와비선형탐색.단어변환;

import java.util.*;

// 강의 풀이 -> DFS
public class Solution2 {
    class Word{
        String word;
        int depth;
        
        Word(String word, int depth) {
            this.word = word;
            this.depth = depth;
        }
    }

    public int solution(String begin, String target, String[] words){
        if (!Arrays.asList(words).contains(target)) return 0;

        Set<String> used = new HashSet<>();

        Stack<Word> stack = new Stack<>();
        stack.add(new Word(begin, 0));
        while (!stack.isEmpty()){
            Word cur = stack.pop();

            if (cur.word.equals(target)) return cur.depth;

            for (String w: words){
                if (!changeable(cur.word, w)) continue;
                if (used.contains(w)) continue;
                
                stack.push(new Word(w, cur.depth + 1));
                used.add(w);
            }
        }

        return -1;
    }

    boolean changeable(String w1, String w2){
        int len = Math.min(w1.length(), w2.length());
        int cnt = 0;
        for (int i = 0; i < len && cnt < 2; i++){
            if (w1.charAt(i) != w2.charAt(i)) cnt++;
        }
        return cnt == 1;
    }
}
