package programmers.List.자연수뒤집어배열로만들기;

import java.util.*;

public class Solution {
    // String 활용
    public int[] solution0(long n) {
        String nStr = Long.toString(n);
        String nStrRvsd = new StringBuilder(nStr).reverse().toString();
        List<Integer> res = new ArrayList<>();
        for(char c: nStrRvsd.toCharArray()){
            res.add(c - '0');
        }
        return res.stream().mapToInt(Integer::intValue).toArray();
    }

    public int[] solution1(long n) {
        List<Integer> list = new LinkedList<>();

        while (n > 0){
            list.add((int)(n % 10));
            n /= 10;
        }

        return list.stream().mapToInt(Integer::intValue).toArray();
    }
}
