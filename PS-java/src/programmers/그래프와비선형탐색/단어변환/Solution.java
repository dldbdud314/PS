package programmers.그래프와비선형탐색.단어변환;

import java.util.*;

class Node{
    String val;
    int level;
    
    public Node(String v, int l){
        val = v;
        level = l;
    }
}

class Solution {
    public int solution(String begin, String target, String[] words) {
        boolean flag = false;
        for (String word: words){
            if (target.equals(word)){
                flag = true;
                break;
            }
        }
        if (!flag) return 0;
        
        Queue<Node> queue = new LinkedList<>();
        queue.offer(new Node(begin, 0));
        
        int res = 0;
        while (!queue.isEmpty()){
            Node cur = queue.poll();
            
            if (cur.val.equals(target)) {
                res = cur.level;
                break;
            }
            
            // 한글자 차이 나는 단어들을 찾아서 큐에 추가하기
            for (String word : words){
                if (valid(word, cur.val)) queue.offer(new Node(word, cur.level + 1));
            }
        }
        
        return res;
    }
    
    boolean valid(String w1, String w2){
        boolean flag = false;
        for (int i = 0; i < w1.length(); i++){
            if (w1.charAt(i) != w2.charAt(i)){
                if (flag) return false;
                flag = true;
            }
        }
        return true;
    }
}
