class Solution(object):
    def climbStairs(self, n, mp={}):
        
        if n == 0 or n == 1:
            return 1
        
        if n in mp:
            return mp[n]
        
        x = self.climbStairs(n - 1, mp)
        y = self.climbStairs(n - 2, mp)
        
        mp[n] = x + y
        return mp[n]