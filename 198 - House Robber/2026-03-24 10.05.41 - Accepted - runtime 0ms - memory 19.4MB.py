class Solution:
    def rob(self, nums: List[int]) -> int:
        ans = 0
        dp = dict()
        def f(ums, ind):
            if ind >= len(nums): return 0
            if ind in dp : return dp[ind]

            skip = f(nums, ind+1)
            take = nums[ind]  + f(nums, ind+2)
            dp[ind] = max(skip, take)
            return max(skip, take)
        return f(nums,0)
