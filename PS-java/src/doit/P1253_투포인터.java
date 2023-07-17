package doit;

import java.io.*;
import java.util.*;

public class P1253_투포인터 {
    static int n;
    static long[] nums;

    private static int two_pointer(int idx){
        int left = 0;
        int right = n - 1;
        while (left < right){
            // 다른 두 수의 합 보장
            if (left == idx) { left++; continue; }
            if (right == idx) { right--; continue; }

            if (nums[left] + nums[right] == nums[idx]) return 1;
            else if (nums[left] + nums[right] > nums[idx]) right--;
            else left++;
        }
        return 0;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        nums = new long[n];

        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++){
            nums[i] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(nums);

        int count = 0;
        for (int i = 0; i < n; i++){
            count += two_pointer(i);
        }

        System.out.println(count);
    }
}
