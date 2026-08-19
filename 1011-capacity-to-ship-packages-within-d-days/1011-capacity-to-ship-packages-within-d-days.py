class Solution:
    def shipWithinDays(self, weights, days):
        l, r = max(weights), sum(weights)

        while l < r:
            mid = (l + r) // 2
            d, total = 1, 0

            for w in weights:
                if total + w > mid:
                    d += 1
                    total = 0
                total += w

            if d <= days:
                r = mid
            else:
                l = mid + 1

        return l