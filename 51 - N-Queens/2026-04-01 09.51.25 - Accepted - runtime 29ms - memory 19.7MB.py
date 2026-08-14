from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["."] * n for _ in range(n)]
        ans = []

        def canPut(r: int, c: int) -> bool:
            for i in range(r):
                if board[i][c] == 'Q':
                    return False

            i, j = r-1, c-1
            while i >= 0 and j >= 0:
                if board[i][j] == 'Q':
                    return False
                j -= 1
                i -= 1

            i, j = r-1, c+1
            while i >= 0 and j < len(board):
                if board[i][j] == 'Q':
                    return False
                i -= 1
                j += 1

            return True   # ✅ missing

        def backtrack(r: int):
            if r == n:
                ans.append(["".join(row) for row in board])
                return

            for c in range(n):
                if canPut(r, c):
                    board[r][c] = 'Q'
                    backtrack(r + 1)
                    board[r][c] = '.'

        backtrack(0)
        return ans