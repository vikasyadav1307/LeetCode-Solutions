class Solution:
    def topKFrequent(self, nums, k):
        count = {}

        # Count frequency
        for num in nums:
            count[num] = count.get(num, 0) + 1

        # Sort by frequency
        sorted_nums = sorted(count, key=count.get, reverse=True)

        return sorted_nums[:k]