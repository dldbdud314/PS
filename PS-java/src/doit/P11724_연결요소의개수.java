package doit;

import java.io.*;
import java.util.*;

public class P11724_연결요소의개수 {
    static ArrayList<Integer>[] graph;
    static boolean[] visited;

    static void dfs(int cur){
        visited[cur] = true;

        for (int v : graph[cur]) {
            if (!visited[v]) dfs(v);
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        graph = new ArrayList[n + 1];
        for (int i = 1; i < n + 1; i++) {
            graph[i] = new ArrayList<>();  // 초기화 주의
        }
        visited = new boolean[n + 1];
        for (int i = 0; i < m; i++){
            st = new StringTokenizer(br.readLine());
            int v1 = Integer.parseInt(st.nextToken());
            int v2 = Integer.parseInt(st.nextToken());
            graph[v1].add(v2);
            graph[v2].add(v1);
        }

        int count = 0;
        for (int i = 1; i < n + 1; i++){
            if (visited[i]) continue;
            dfs(i);
            count++;
        }
        System.out.println(count);
    }
}
