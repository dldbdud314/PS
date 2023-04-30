package programmers.Stack_Queue.주식가격;

import java.util.*;

// Stack 
class Solution {
    
    public int[] solution(int[] prices) {
        int[] res = new int[prices.length];
        Stack<List<Integer>> stack = new Stack<>();
        for(int i = 0; i < prices.length; i++){
            while (!stack.isEmpty() && prices[i] < stack.peek().get(0)){
                List<Integer> pair = stack.pop();
                res[pair.get(1)] = i - pair.get(1);
            }
            stack.push(List.of(prices[i], i));
        }
        
        while (!stack.isEmpty()){
            List<Integer> pair = stack.pop();
            res[pair.get(1)] = prices.length - pair.get(1) - 1;
        }
        
        return res;
    }
}