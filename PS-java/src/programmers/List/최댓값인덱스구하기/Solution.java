package programmers.List.최댓값인덱스구하기;

import java.util.*;
import java.util.stream.*;

class Solution {
    public int[] solution0(int[] arr) {
        int max = -9999;
        
        List<Integer> idxList = new ArrayList<>();
        for(int i = 0; i < arr.length; i++){
            if (max < arr[i]){
                max = arr[i];
                idxList = new ArrayList<>(Arrays.asList(i));
            }
            else if (max == arr[i]){
                idxList.add(i);
            }
        }

        return idxList.stream()
            .mapToInt(Integer::intValue)
            .toArray();
    }

    // Stream 활용하기
    public int[] solution1(int[] arr) {
        int max = Arrays.stream(arr).max().getAsInt();

        return IntStream.range(0, arr.length)
            .filter(i -> arr[i] == max)
            .toArray();
    } 
}
