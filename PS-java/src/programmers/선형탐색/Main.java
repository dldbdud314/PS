package programmers.선형탐색;

import java.util.*;

class MyData implements Comparable<MyData>{
    int v;

    public MyData(int v){
        this.v = v;
    }

    @Override
    public String toString(){
        return "" + v;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        MyData myData = (MyData)o;
        return v == myData.v;
    }

    @Override
    public int hashCode() {
        return Objects.hash(v);
    }

    @Override
    public int compareTo(MyData o) {
        return v - o.v;
    }
}

public class Main {
    public static void main(String[] args) {
        List<MyData> list = new LinkedList<>();

        Random r = new Random();
        for (int i = 1; i <= 100; i++) list.add(new MyData(r.nextInt(100)));
    
        System.out.println(list);
    
        // Linear Search
        int idx = list.indexOf(new MyData(63));
        System.out.println(idx);

        List<MyData> list2 = new LinkedList<>();
        for (int i = 1; i <= 100; i++) list2.add(new MyData(i));

        // 정렬된 데이터에 대해서 Binary Search
        int idx2 = Collections.binarySearch(list2, new MyData(63));
        System.out.println(idx2);
    }

}

/*
 * Search는 indexOf, contains, remove 같은 곳에서 이미 구현되어 있음 : 완전 탐색
 * equals가 제공될 필요가 있다 !
 * 
 * 이진탐색은 Collections.binarySearch 활용하기 (선 정렬)
 * 대소 관계 비교를 위해 Comparable의 compareTo가 구현되어야 !
 */