package 이코테.카드정렬하기;

import java.util.*;

public class Main {
    public static int n;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();

        PriorityQueue<Integer> pq = new PriorityQueue<>();
        // 힙(Heap)에 초기 카드 묶음을 모두 삽입
        for (int i = 0; i < n; i++) {
            pq.offer(sc.nextInt());
        }

        int total = 0;
        while (pq.size() > 1){
            int n1 = pq.poll();
            int n2 = pq.poll();

            int sum = n1 + n2;
            
            total += sum;
            pq.offer(sum);
        }

        System.out.println(total);

        sc.close();
    }
}
