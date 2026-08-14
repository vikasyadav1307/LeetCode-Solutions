from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum = nums[0]
        max_sum = nums[0]

        for i in range(1, len(nums)):
            # either start new subarray or continue previous
            current_sum = max(nums[i], current_sum + nums[i])
            
            # update maximum sum found so far
            max_sum = max(max_sum, current_sum)

        return max_sum