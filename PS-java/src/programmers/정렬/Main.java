package programmers.정렬;

import java.util.*;

class MyData implements Comparable<MyData>{
    int v;

    MyData(int v){
        this.v = v;
    }

    @Override
    public String toString() {
        return String.valueOf(v);
    }

    @Override
    public int compareTo(MyData o) {
        return Integer.compare(this.v, o.v);
    }
}

public class Main {
    public static void main(String[] args) {
        List<MyData> list = new LinkedList<>();

        Random r = new Random();
        for (int i = 0; i < 20; i++) list.add(new MyData(r.nextInt(50)));

        list.sort((o1, o2) -> o1.v - o2.v);

        System.out.println(list);
    }

}
