class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        # Do not return anything, modify board in-place instead.

        rowset = {}
        colset = {}
        gridset = {}

        for i in range(10):
            rowset[i] = [0] * 10
            colset[i] = [0] * 10
            gridset[i] = [0] * 10

        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num != '.':
                    num = ord(num) - ord('0')
                    rowset[i][num] = 1
                    colset[j][num] = 1
                    sr = 3 * (i // 3)
                    sc = 3 * (j // 3)
                    gridset[sr + sc // 3][num] = 1

        def solve(row, col):
            if row == 9:
                return True

            if col == 9:
                return solve(row + 1, 0)

            if board[row][col] != '.':
                return solve(row, col + 1)

            for num in '123456789':
                sr = (row // 3) * 3
                t = ord(num) - ord('0')

                if rowset[row][t] == 0 and colset[col][t] == 0 and gridset[sr + col // 3][t] == 0:
                    board[row][col] = num
                    rowset[row][t] = 1
                    colset[col][t] = 1
                    gridset[sr + col // 3][t] = 1

                    if solve(row, col + 1):
                        return True

                    board[row][col] = '.'
                    rowset[row][t] = 0
                    colset[col][t] = 0
                    gridset[sr + col // 3][t] = 0

            return False

        solve(0, 0)