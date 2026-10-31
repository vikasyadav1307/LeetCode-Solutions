
class Solution {
    public int uniquePaths(int[][] grid) {
        int m = grid.length;
        int n = grid[0].length;

        int MOD = 1_000_000_007;

        long[][] ways = new long[m][n];
        long[][] right = new long[m][n];
        long[][] down = new long[m][n];

        // Traverse from bottom-right to top-left
        for (int i = m - 1; i >= 0; i--) {
            for (int j = n - 1; j >= 0; j--) {

                // Destination
                if (i == m - 1 && j == n - 1) {
                    ways[i][j] = 1;
                    right[i][j] = 1;
                    down[i][j] = 1;
                    continue;
                }

                if (grid[i][j] == 1) {
                    // Mirror:
                    // Entering from right -> reflected down
                    if (i + 1 < m) {
                        right[i][j] = down[i + 1][j];
                    }

                    // Entering from down -> reflected right
                    if (j + 1 < n) {
                        down[i][j] = right[i][j + 1];
                    }

                } else {
                    // Empty cell: choose right or down
                    long r = (j + 1 < n) ? right[i][j + 1] : 0;
                    long d = (i + 1 < m) ? down[i + 1][j] : 0;

                    ways[i][j] = (r + d) % MOD;

                    right[i][j] = ways[i][j];
                    down[i][j] = ways[i][j];
                }
            }
        }

        return (int) ways[0][0];
    }
}
