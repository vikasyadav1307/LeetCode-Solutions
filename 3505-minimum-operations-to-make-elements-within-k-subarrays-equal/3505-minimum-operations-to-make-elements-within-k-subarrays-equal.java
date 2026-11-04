
import java.util.*;

class Solution {

    class Fenwick {
        int n;
        long[] count;
        long[] sum;

        Fenwick(int n) {
            this.n = n;
            count = new long[n + 1];
            sum = new long[n + 1];
        }

        void add(int i, long c, long s) {
            while (i <= n) {
                count[i] += c;
                sum[i] += s;
                i += i & -i;
            }
        }

        long queryCount(int i) {
            long result = 0;
            while (i > 0) {
                result += count[i];
                i -= i & -i;
            }
            return result;
        }

        long querySum(int i) {
            long result = 0;
            while (i > 0) {
                result += sum[i];
                i -= i & -i;
            }
            return result;
        }

        // Find the kth smallest element
        int kth(int k) {
            int idx = 0;

            for (int bit = Integer.highestOneBit(n);
                 bit > 0; bit >>= 1) {

                int next = idx + bit;

                if (next <= n && count[next] < k) {
                    idx = next;
                    k -= (int) count[next];
                }
            }

            return idx + 1;
        }
    }

    public long minOperations(int[] nums, int x, int k) {

        int n = nums.length;

        // Coordinate compression
        int[] sorted = nums.clone();
        Arrays.sort(sorted);

        int m = 0;

        for (int v : sorted) {
            if (m == 0 || sorted[m - 1] != v) {
                sorted[m++] = v;
            }
        }

        int[] values = Arrays.copyOf(sorted, m);

        Fenwick bit = new Fenwick(m);

        // Calculate cost of every window of size x
        long[] cost = new long[n - x + 1];

        for (int i = 0; i < x; i++) {
            int id = Arrays.binarySearch(values, nums[i]) + 1;
            bit.add(id, 1, nums[i]);
        }

        for (int s = 0; s <= n - x; s++) {

            // Find median
            int medianId = bit.kth((x + 1) / 2);
            long median = values[medianId - 1];

            // Calculate cost using prefix counts and sums
            long leftCount = bit.queryCount(medianId);
            long leftSum = bit.querySum(medianId);

            long totalSum = bit.querySum(m);

            long rightCount = x - leftCount;
            long rightSum = totalSum - leftSum;

            cost[s] =
                median * leftCount - leftSum
                + rightSum - median * rightCount;

            // Slide window
            if (s < n - x) {

                int removeId =
                    Arrays.binarySearch(values, nums[s]) + 1;

                int addId =
                    Arrays.binarySearch(values, nums[s + x]) + 1;

                bit.add(removeId, -1, -nums[s]);
                bit.add(addId, 1, nums[s + x]);
            }
        }

        // Dynamic Programming
        long INF = Long.MAX_VALUE / 4;

        long[] prev = new long[n + 1];
        long[] curr = new long[n + 1];

        for (int t = 1; t <= k; t++) {

            Arrays.fill(curr, INF);

            for (int i = 1; i <= n; i++) {

                // Option 1: Skip current element
                curr[i] = curr[i - 1];

                // Option 2: Take a subarray of size x
                if (i >= x && prev[i - x] != INF) {

                    long take =
                        prev[i - x] + cost[i - x];

                    curr[i] = Math.min(curr[i], take);
                }
            }

            long[] temp = prev;
            prev = curr;
            curr = temp;
        }

        return prev[n];
    }
}
