class Solution(object):
    def sortedSquares(self, nums):
        res=[]
        for i in nums:
            res.append(i*i)
        res.sort()
        return res
        