class Solution:
    def removeInvalidParentheses(self, s):

        ans = []

        # Count minimum removals needed
        left = 0
        right = 0

        for ch in s:
            if ch == '(':
                left += 1
            elif ch == ')':
                if left > 0:
                    left -= 1
                else:
                    right += 1

        def dfs(s, start, left_rem, right_rem):

            if left_rem == 0 and right_rem == 0:

                balance = 0

                for ch in s:
                    if ch == '(':
                        balance += 1
                    elif ch == ')':
                        balance -= 1

                        if balance < 0:
                            return

                if balance == 0:
                    ans.append(s)

                return

            for i in range(start, len(s)):

                # Skip duplicate removals
                if i > start and s[i] == s[i - 1]:
                    continue

                # Remove '('
                if left_rem > 0 and s[i] == '(':
                    dfs(
                        s[:i] + s[i + 1:],
                        i,
                        left_rem - 1,
                        right_rem
                    )

                # Remove ')'
                if right_rem > 0 and s[i] == ')':
                    dfs(
                        s[:i] + s[i + 1:],
                        i,
                        left_rem,
                        right_rem - 1
                    )

        dfs(s, 0, left, right)

        return ans