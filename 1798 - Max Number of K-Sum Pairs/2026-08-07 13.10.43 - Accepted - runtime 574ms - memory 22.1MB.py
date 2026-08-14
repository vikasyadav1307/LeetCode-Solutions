class Solution:
    def maxOperations(self, nums, k):
        freq = {}
        ans = 0
        for num in nums:
            need = k - num
            if freq.get(need, 0) > 0:
                ans += 1
                freq[need] -= 1
            else:
                freq[num] = freq.get(num, 0) + 1
        return ans