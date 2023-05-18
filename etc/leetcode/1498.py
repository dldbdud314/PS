"""
1498. Number of Subsequences That Satisfy the Given Sum Condition (풀참)
- two pointer, set (math)
"""
from typing import List


class Solution:

    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        mod = 10 ** 9 + 7

        res = 0
        left, right = 0, len(nums) - 1
        while left <= right:
            if nums[left] + nums[right] > target:
                right -= 1
            else:
                res += 2 ** (right - left)
                res %= mod
                left += 1

        return res
