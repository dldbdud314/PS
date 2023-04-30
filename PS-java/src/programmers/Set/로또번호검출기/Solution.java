package programmers.Set.로또번호검출기;

import java.util.*;
import java.util.stream.*;

public class Solution {
    public boolean solution(int[] lotto) {
        Set<Integer> lSet = Arrays.stream(lotto)
                                .boxed()
                                .collect(Collectors.toSet());
        if (lSet.size() == lotto.length){
            for (int n: lSet){
                if (1 <= n && n <= 45) return true;
            }
        }
        return false;
    }
}
