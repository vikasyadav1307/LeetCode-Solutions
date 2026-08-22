class Solution:
    def checkDivisibility(self, n):
        original = n
        s, p = 0, 1

        while n:
            digit = n % 10
            s += digit
            p *= digit
            n //= 10

        return original % (s + p) == 0