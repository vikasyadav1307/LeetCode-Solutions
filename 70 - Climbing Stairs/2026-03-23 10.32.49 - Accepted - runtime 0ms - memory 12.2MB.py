class Solution(object):
    def climbStairs(self, n):
        mp = {}
        mp[0] = 1
        mp[1] = 1
        
        for i in range(2, n + 1):
            mp[i] = mp[i - 1] + mp[i - 2]
        
        return mp[n]