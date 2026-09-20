class Solution:
    def reverseDegree(self, s):
        alphabet = "abcdefghijklmnopqrstuvwxyz"

        ans = 0

        for i in range(len(s)):
            for j in range(26):
                if s[i] == alphabet[j]:
                    ans += (26 - j) * (i + 1)
                    break

        return ans