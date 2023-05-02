package programmers.그래프와비선형탐색.타겟넘버;

// 강의 풀이 -> recursive 
// 허어어 코드가 아름다워!! 8_8
public class Solution2 {
    public int solution(int[] numbers, int target) {
        return sumCount(numbers, target, 0, 0);
    }

    int sumCount(int[] numbers, int target, int idx, int sum){
        if (idx == numbers.length){
            if (sum == target) return 1;
            return 0;
        }

        return sumCount(numbers, target, idx + 1, sum + numbers[idx]) + sumCount(numbers, target, idx + 1, sum - numbers[idx]);
    }
}