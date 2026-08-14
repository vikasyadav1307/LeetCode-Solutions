class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        ans = [1] * n

        # Prefix product
        for i in range(1, n):
            ans[i] = ans[i - 1] * nums[i - 1]

        # Suffix product
        suffix = 1
        for i in range(n - 1, -1, -1):
            ans[i] *= suffix
            suffix *= nums[i]

        return ans