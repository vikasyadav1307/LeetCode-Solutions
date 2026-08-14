class Solution:
    def searchRange(self, nums, target):

        def bs(left):
            l, r = 0, len(nums) - 1
            ans = -1
            while l <= r:
                m = (l + r) // 2
                if nums[m] == target:
                    ans = m
                    if left:
                        r = m - 1
                    else:
                        l = m + 1
                elif nums[m] < target:
                    l = m + 1
                else:
                    r = m - 1
            return ans

        return [bs(True), bs(False)]