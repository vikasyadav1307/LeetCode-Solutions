
import java.util.*;

class Solution {
    public int shortestPath(int n, int[][] edges, String labels, int k) {

        // Build adjacency list
        List<int[]>[] adj = new ArrayList[n];

        for (int i = 0; i < n; i++) {
            adj[i] = new ArrayList<>();
        }

        for (int[] e : edges) {
            adj[e[0]].add(new int[]{e[1], e[2]});
        }

        // dist[node][count]
        long[][] dist = new long[n][k + 1];

        for (long[] row : dist) {
            Arrays.fill(row, Long.MAX_VALUE);
        }

        // {cost, node, consecutive count}
        PriorityQueue<long[]> pq = new PriorityQueue<>(
            (a, b) -> Long.compare(a[0], b[0])
        );

        dist[0][1] = 0;
        pq.offer(new long[]{0, 0, 1});

        while (!pq.isEmpty()) {

            long[] curr = pq.poll();

            long cost = curr[0];
            int node = (int) curr[1];
            int count = (int) curr[2];

            // Skip outdated states
            if (cost != dist[node][count]) {
                continue;
            }

            // Destination reached
            if (node == n - 1) {
                return (int) cost;
            }

            // Explore neighbours
            for (int[] next : adj[node]) {

                int v = next[0];
                int weight = next[1];

                int newCount;

                if (labels.charAt(node) == labels.charAt(v)) {
                    newCount = count + 1;
                } else {
                    newCount = 1;
                }

                // Invalid consecutive sequence
                if (newCount > k) {
                    continue;
                }

                long newCost = cost + weight;

                if (newCost < dist[v][newCount]) {

                    dist[v][newCount] = newCost;

                    pq.offer(new long[]{
                        newCost, v, newCount
                    });
                }
            }
        }

        return -1;
    }
}
