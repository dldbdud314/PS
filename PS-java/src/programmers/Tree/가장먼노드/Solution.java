package programmers.Tree.가장먼노드;

import java.util.*;

class Node{
    int node;
    List<Node> links = new LinkedList<>();
    int dist = 0;
    boolean visit = false;
    
    Node(int node){
        this.node = node;
    }
}

class Solution {
    public int solution(int n, int[][] edge) {
        List<Node> graph = new ArrayList<>(n);
        for (int i = 1; i <= n; i++) graph.add(new Node(i));
        
        for (int[] e : edge){
            Node n1 = graph.get(e[0] - 1), n2 = graph.get(e[1] - 1);
            n1.links.add(n2);
            n2.links.add(n1);
        }
        
        Queue<Node> queue = new LinkedList<>();
        Node start = graph.get(0);
        start.visit = true;
        queue.add(start);
        
        int maxDist = 0;
        while (!queue.isEmpty()){
            Node now = queue.poll();
            
            for (Node nxt : now.links){
                if (!nxt.visit){
                    nxt.visit = true;
                    nxt.dist = now.dist + 1;
                    
                    queue.offer(nxt);
                    
                    maxDist = Math.max(maxDist, nxt.dist);
                }
            }
            
        }
        
        int cnt = 0;
        for (Node x : graph){
            if (x.dist == maxDist) cnt++;
        }
        
        return cnt;
    }
}
