"""
1. Two sum
- hash table
"""
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        record = dict()
        for k in range(len(nums)):
            cur = nums[k]
            other = target - cur
            if other in record:
                return [k, record[other]]
            record[cur] = k
            