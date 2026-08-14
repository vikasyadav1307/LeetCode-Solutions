class Solution(object):
    def fib(self, n):
        mp = {}
        
        if n <= 1:
            return n
        
        if n in mp:
            return mp[n]
        
        x = self.fib(n - 1)
        y = self.fib(n - 2)
        
        mp[n] = x + y
        return mp[n]