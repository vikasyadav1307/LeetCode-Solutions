class Solution(object):
    def maxSubArray(self, nums):
        current_sum = nums[0]
        max_sum = nums[0]

        for i in range(1, len(nums)):
            # choose: start new subarray or continue
            current_sum = max(nums[i], current_sum + nums[i])

            # update maximum
            max_sum = max(max_sum, current_sum)

        return max_sum