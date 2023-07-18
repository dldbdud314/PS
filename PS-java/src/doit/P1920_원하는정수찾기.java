package doit;

import java.io.*;
import java.util.*;

public class P1920_원하는정수찾기 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int n = Integer.parseInt(br.readLine());
        int[] datas = new int[n];
        st = new StringTokenizer(br.readLine());
        for(int i = 0; i < n; i++) datas[i] = Integer.parseInt(st.nextToken());
        Arrays.sort(datas);

        int m = Integer.parseInt(br.readLine());
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < m; i++){
            int num = Integer.parseInt(st.nextToken());
            int idx = Arrays.binarySearch(datas, num);
            System.out.println(idx >= 0 ? 1 : 0);
        }
    }
}
