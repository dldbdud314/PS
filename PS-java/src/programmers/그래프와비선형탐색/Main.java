package programmers.그래프와비선형탐색;

import java.util.*;

class Node{
    String name;
    List<Node> links;
    boolean visited;
    
    public Node(String name){
        this.name = name;
        this.links = new LinkedList<>();
    }

    void link(Node node){
        links.add(node);
    }

    void visit(){
        this.visited = true;
    }

    void unvisit(){
        this.visited = false;
    }

    boolean isVisited(){
        return this.visited;
    }

    @Override
    public String toString(){
        return name;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Node node = (Node) o;
        return Objects.equals(name, node.name);
    }

    @Override
    public int hashCode() {
        return Objects.hash(name);
    }
}

public class Main {
    public static void main(String[] args) {
        Node A = new Node("A");
        Node B = new Node("B");
        Node C = new Node("C");
        Node D = new Node("D");
        Node E = new Node("E");

        A.link(B);
        A.link(D);
        B.link(A);
        B.link(C);
        B.link(E);
        C.link(B);
        C.link(D);
        D.link(A);
        D.link(C);
        D.link(E);
        E.link(B);
        E.link(D);

        Node target = E;
        
        // bfs
        Queue<Node> queue = new LinkedList<>();
        queue.offer(A);

        while(!queue.isEmpty()){
            Node cur = queue.poll();
            cur.visit();
            System.out.println(cur);

            if (cur.equals(target)){
                System.out.println("FOUND!! " + cur);
                break;
            }

            // cur.links.stream()
            //     .filter(l -> !l.isVisited() && !queue.contains(l))
            //     .forEach(queue::offer);

            for (Node l : cur.links){
                if (l.isVisited()) continue;
                if (queue.contains(l)) continue;
                queue.offer(l);
            }
        }

        A.unvisit(); B.unvisit(); C.unvisit(); D.unvisit(); E.unvisit();
        
        // dfs
        Stack<Node> stack = new Stack<>();
        stack.push(A);

        while(!stack.isEmpty()){
            Node cur2 = stack.pop();
            cur2.visit();
            System.out.println(cur2);

            if (cur2.equals(target)){
                System.out.println("FOUND!! " + cur2);
                break;
            }
            
            for (Node l : cur2.links){
                if (l.isVisited()) continue;
                if (stack.contains(l)) continue;
                stack.push(l);
            }
        }

    }
}
