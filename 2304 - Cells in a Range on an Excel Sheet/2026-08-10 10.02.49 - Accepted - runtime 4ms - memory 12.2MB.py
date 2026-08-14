class Solution:
    def cellsInRange(self, s):
        ans = []

        for col in range(ord(s[0]), ord(s[3]) + 1):
            for row in range(int(s[1]), int(s[4]) + 1):
                ans.append(chr(col) + str(row))

        return ans