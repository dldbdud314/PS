package programmers.Map;

import java.util.*;

class Main{
    public static void main(String[] args) {

        Map<String, Integer> map = new Hashtable<>();
        map.put("A", 1);
        map.put("A", 2);
        map.putIfAbsent("B", 4);

        map.remove("A");

        System.out.println(map.replace("B", 3, 2));
        System.out.println(map.getOrDefault("A", -1));

        map.putAll(Map.of("K", 9, "F", 3));
        System.out.println(map.keySet());
        System.out.println(map.values());
    }
}