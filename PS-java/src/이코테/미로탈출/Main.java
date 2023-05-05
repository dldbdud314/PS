package 이코테.미로탈출;

import java.util.*;

class Node{
    int x;
    int y;
    int d;

    Node(int x, int y, int d){ this.x = x; this.y = y; this.d = d; }

    public String toString() { return "" + x + ", " + y + ", " + d; }
}

public class Main {
    private static int n, m;
    private static int[][] map;
    private static boolean[][] visited;
    private static int[] dx = {0, 1, 0, -1}, dy = {1, 0, -1, 0};

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // N, M을 공백을 기준으로 구분하여 입력 받기
        n = sc.nextInt();
        m = sc.nextInt();
        sc.nextLine();

        map = new int[n][m];
        // 2차원 리스트의 맵 정보 입력 받기
        for (int i = 0; i < n; i++) {
            String str = sc.nextLine();
            for (int j = 0; j < m; j++) {
                map[i][j] = str.charAt(j) - '0';
            }
        }

        visited = new boolean[n][m];
        int dist = 0;

        Queue<Node> queue = new LinkedList<>();
        queue.add(new Node(0, 0, 1));
        visited[0][0] = true;
        while(!queue.isEmpty()){
            Node cur = queue.poll();

            if (cur.x == n - 1 && cur.y == m - 1){
                dist = cur.d;
                break;
            }

            for (int i = 0; i < 4; i++){
                int nx = cur.x + dx[i], ny = cur.y + dy[i];
                if (nx < 0 || nx >= n || ny < 0 || ny >= m) continue;
                
                if (!visited[nx][ny] && map[nx][ny] == 1){
                    visited[nx][ny] = true;
                    queue.offer(new Node(nx, ny, cur.d + 1));
                }
            }
        }

        System.out.println(dist);

        sc.close();
    }
}
