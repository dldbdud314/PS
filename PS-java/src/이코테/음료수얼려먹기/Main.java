package 이코테.음료수얼려먹기;

import java.util.*;

public class Main{

    private static int n, m;
    private static int[][] matrix;
    private static boolean[][] visited;

    private static int[] dx = {0, 1, 0, -1};
    private static int[] dy = {1, 0, -1, 0};

    private static void dfs(int cx, int cy){
        visited[cx][cy] = true;

        for (int i = 0; i < 4; i++){
            int nx = cx + dx[i], ny = cy + dy[i];

            if (nx < 0 || nx >= n || ny < 0 || ny >= m) continue;
            if (matrix[nx][ny] == 0 && !visited[nx][ny]) dfs(nx, ny);
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // N, M을 공백을 기준으로 구분하여 입력 받기
        n = sc.nextInt();
        m = sc.nextInt();
        sc.nextLine();

        matrix = new int[n][m];
        // 2차원 리스트의 맵 정보 입력 받기
        for (int i = 0; i < n; i++) {
            String str = sc.nextLine();
            for (int j = 0; j < m; j++) {
                matrix[i][j] = str.charAt(j) - '0';
            }
        }

        int cnt = 0;
        visited = new boolean[n][m];
        for (int i = 0; i < n; i++){
            for (int j = 0; j < m; j++){
                if (!visited[i][j] && matrix[i][j] == 0){
                    dfs(i, j);
                    cnt++;
                }
            }
        }

        System.out.println(cnt);
        
        sc.close();
    }
}