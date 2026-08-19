class Solution:
    def smallestDivisor(self, nums, threshold):
        left, right = 1, max(nums)

        while left < right:
            mid = (left + right) // 2

            total = sum((x + mid - 1) // mid for x in nums)

            if total <= threshold:
                right = mid
            else:
                left = mid + 1

        return left