package doit;

import java.io.*;
import java.util.*;

public class P11003_최솟값찾기 {
    static class Node{
        long idx;
        int val;

        Node(long idx, int val){
            this.idx = idx;
            this.val = val;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());
        long n = Long.parseLong(st.nextToken());
        long l = Long.parseLong(st.nextToken());
        st = new StringTokenizer(br.readLine());

        Deque<Node> deque = new LinkedList<>();
        for (long i = 0; i < n; i++){
            int curVal = Integer.parseInt(st.nextToken());

            if (deque.isEmpty()) deque.addLast(new Node(i, curVal));
            else {
                // 맨 앞 인덱스 확인해서 윈도우만큼 poll
                if (i - deque.getFirst().idx >= l) deque.pollFirst();
                // 맨 뒤와 비교해가며 poll -> deque 정렬
                while (!deque.isEmpty() && deque.getLast().val > curVal) deque.pollLast();
                // 현재 값 추가
                deque.offerLast(new Node(i, curVal));
            }
            // 첫번째 값 == 최솟값 보장
            bw.write(deque.getFirst().val + " ");
        }
        bw.flush();
        bw.close();
    }
}
