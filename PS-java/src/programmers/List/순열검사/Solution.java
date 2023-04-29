package programmers.List.순열검사;

import java.util.*;

public class Solution {
    public boolean solution0(int[] arr){
        Arrays.sort(arr);
        if (arr[arr.length - 1] != arr.length){
            return false;
        }

        for (int n = 1; n < arr.length + 1; n++){
            if (n != arr[n - 1]){
                return false;
            }
        }
        
        return true;
    }

    // 미리 답 짜 맞추고 비교하기
    public boolean solution1(int[] arr){
        int[] ans = new int[arr.length];
        for (int i = 0; i < arr.length; i++){
            ans[i] = i + 1;
        }
        Arrays.sort(arr);

        return Arrays.equals(arr, ans);
    }
}
