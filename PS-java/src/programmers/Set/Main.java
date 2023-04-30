package programmers.Set;

import java.util.*;

public class Main {
    public static void main(String[] args) {
        Set<Integer> set = new HashSet<>();

        set.add(1);
        set.add(1);
        set.add(2);
        set.add(4);

        set.remove(1);

        System.out.println(set);
        System.out.println(set.contains(1));

        Set<Integer> set2 = new HashSet<>();
        set.add(5);
        set.add(6);

        set.addAll(set2);  // 합집합
        System.out.println(set);

        set.removeAll(Set.of(3, 4));  // 차집합
        System.out.println(set);

        set.retainAll(Set.of(5, 6));  // 교집합
        System.out.println(set);
    }

}
