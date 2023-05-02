package programmers.그래프와비선형탐색.게임맵최단거리;

import java.util.*;

class Point{
    int x;
    int y;
    int d;
    
    Point(int x, int y, int d){
        this.x = x;
        this.y = y;
        this.d = d;
    }
}

class Solution {
    
    public int solution(int[][] maps) {
        int n = maps.length, m = maps[0].length;
        
        int[] dx = {0, 1, 0, -1}, dy = {1, 0, -1, 0};
        
        Queue<Point> queue = new LinkedList<>();
        queue.offer(new Point(0, 0, 1));
        boolean[][] visited = new boolean[n][m];
        visited[0][0] = true;

        int res = -1;
        while (!queue.isEmpty()){
            Point point = queue.poll();
            
            int cx = point.x, cy = point.y, cd = point.d;
            
            if (cx == n - 1 && cy == m - 1){
                res = cd;
                break;
            }
            
            for (int i = 0; i < 4; i++){
                int nx = cx + dx[i], ny = cy + dy[i];
                if ((0 <= nx && nx < n) && (0 <= ny && ny < m) && maps[nx][ny] == 1 && !visited[nx][ny]){
                    visited[nx][ny] = true;
                    queue.offer(new Point(nx, ny, cd + 1));
                }
            }
        }

        return res;
    }
}
