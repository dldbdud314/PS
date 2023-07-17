package doit;

import java.io.*;
import java.util.*;

public class P11659_구간합구하기{
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        long[] sums = new long[n + 1];
        st = new StringTokenizer(br.readLine());
        // 누적
        for (int i = 1; i < n + 1; i++){
            sums[i] = sums[i - 1] + Integer.parseInt(st.nextToken());
        }

        // 구간합 구하기
        for (int i = 0; i < m; i++){
            st = new StringTokenizer(br.readLine());
            int n1 = Integer.parseInt(st.nextToken());
            int n2 = Integer.parseInt(st.nextToken());
            System.out.println(sums[n2] - sums[n1 - 1]);
        }

    }
}