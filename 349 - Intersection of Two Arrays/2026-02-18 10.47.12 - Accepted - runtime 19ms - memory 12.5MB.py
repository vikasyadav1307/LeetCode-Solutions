class Solution(object):
    def intersection(self, nums1, nums2):
        res = []

        for i in nums1:
            if i in nums2 and i not in res:
                res.append(i)

        return res