package doit;

import java.io.*;
import java.util.*;

public class P1260_DFS와BFS {
    static ArrayList<Integer>[] graph;

    static void dfs(boolean[] vis, int cur){
        vis[cur] = true;
        System.out.print(cur + " ");
        for (int v : graph[cur]){
            if (!vis[v]) dfs(vis, v);
        }
    }

    static void bfs(boolean[] vis, int start){
        Queue<Integer> queue = new LinkedList<>();
        queue.add(start);
        vis[start] = true;

        while (!queue.isEmpty()){
            int cur = queue.poll();
            System.out.print(cur + " ");

            for (int v : graph[cur]){
                if (!vis[v]) { queue.offer(v); vis[v] = true; }
            }
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        graph = new ArrayList[n + 1];
        for (int i = 1; i < n + 1; i++) graph[i] = new ArrayList<>();
        int start = Integer.parseInt(st.nextToken());
        for (int i = 0; i < m; i++){
            st = new StringTokenizer(br.readLine());
            int v1 = Integer.parseInt(st.nextToken());
            int v2 = Integer.parseInt(st.nextToken());
            graph[v1].add(v2);
            graph[v2].add(v1);
        }
        for (int i = 1; i < n + 1; i++) Collections.sort(graph[i]);

        // dfs
        boolean[] vis1 = new boolean[n + 1];
        dfs(vis1, start);
        System.out.println();

        // bfs
        boolean[] vis2 = new boolean[n + 1];
        bfs(vis2, start);
    }
}
