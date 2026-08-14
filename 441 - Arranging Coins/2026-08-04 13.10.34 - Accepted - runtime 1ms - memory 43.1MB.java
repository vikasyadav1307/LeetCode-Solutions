class Solution {
    public int arrangeCoins(int n) {
        int l = 1;
        int r = n;
        int ans = 0;

        while (l <= r) {
            int m = l + (r - l) / 2;

            long coins = (long) m * (m + 1) / 2;

            if (coins == n) {
                return m;
            } else if (coins < n) {
                ans = m;
                l = m + 1;
            } else {
                r = m - 1;
            }
        }

        return ans;
    }
}