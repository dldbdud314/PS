package programmers.그래프와비선형탐색.네트워크;

class Solution {
    void dfs(int n, int[][] computers, int i, boolean[] visited){
        visited[i] = true;
        
        for (int j = 0; j < n; j++){
            if (i != j && !visited[j] && computers[i][j] == 1) dfs(n, computers, j, visited);
        }
    }
    
    public int solution(int n, int[][] computers) {
        boolean[] visited = new boolean[n];
        
        int cnt = 0;
        for (int i = 0; i < n; i++){
            if (!visited[i]) {
                dfs(n, computers, i, visited);
                cnt++;
            }
        }

        return cnt;
    }
}
