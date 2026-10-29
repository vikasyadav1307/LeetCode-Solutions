import java.util.*;

class Solution {
    private List<List<Integer>> adj;
    private int[] parent, depth, heavy, head, pos, invPos;
    private int curPos;
    private int[] tree;
    private int[] val;

    public List<Boolean> palindromePath(int n, int[][] edges, String s, String[] queries) {
        adj = new ArrayList<>();
        for (int i = 0; i < n; i++) adj.add(new ArrayList<>());
        for (int[] edge : edges) {
            adj.get(edge[0]).add(edge[1]);
            adj.get(edge[1]).add(edge[0]);
        }

        parent = new int[n];
        depth = new int[n];
        heavy = new int[n];
        head = new int[n];
        pos = new int[n];
        invPos = new int[n];
        val = new int[n];
        
        Arrays.fill(heavy, -1);
        
        dfs1(0, -1, 0);
        curPos = 0;
        dfs2(0, 0);

        for (int i = 0; i < n; i++) {
            val[i] = 1 << (s.charAt(i) - 'a');
        }

        tree = new int[4 * n];
        build(1, 0, n - 1);

        List<Boolean> ans = new ArrayList<>();
        for (String qStr : queries) {
            String[] parts = qStr.split(" ");
            if (parts[0].equals("update")) {
                int u = Integer.parseInt(parts[1]);
                int newMask = 1 << (parts[2].charAt(0) - 'a');
                val[u] = newMask;
                update(1, 0, n - 1, pos[u], newMask);
            } else {
                int u = Integer.parseInt(parts[1]);
                int v = Integer.parseInt(parts[2]);
                int pathMask = queryPath(u, v, n);
                // A path forms a palindrome if at most one bit is set in the XOR sum
                boolean isPalindrome = (pathMask & (pathMask - 1)) == 0;
                ans.add(isPalindrome);
            }
        }
        return ans;
    }

    private int dfs1(int u, int p, int d) {
        parent[u] = p;
        depth[u] = d;
        int size = 1;
        int maxSubtree = 0;
        for (int v : adj.get(u)) {
            if (v != p) {
                int subtreeSize = dfs1(v, u, d + 1);
                size += subtreeSize;
                if (subtreeSize > maxSubtree) {
                    maxSubtree = subtreeSize;
                    heavy[u] = v;
                }
            }
        }
        return size;
    }

    private void dfs2(int u, int h) {
        head[u] = h;
        pos[u] = curPos;
        invPos[curPos++] = u;
        if (heavy[u] != -1) {
            dfs2(heavy[u], h);
        }
        for (int v : adj.get(u)) {
            if (v != parent[u] && v != heavy[u]) {
                dfs2(v, v);
            }
        }
    }

    private void build(int node, int start, int end) {
        if (start == end) {
            int u = invPos[start];
            tree[node] = val[u];
            return;
        }
        int mid = (start + end) / 2;
        build(2 * node, start, mid);
        build(2 * node + 1, mid + 1, end);
        tree[node] = tree[2 * node] ^ tree[2 * node + 1];
    }
    
    private void update(int node, int start, int end, int idx, int newVal) {
        if (start == end) {
            tree[node] = newVal;
            return;
        }
        int mid = (start + end) / 2;
        if (idx <= mid) {
            update(2 * node, start, mid, idx, newVal);
        } else {
            update(2 * node + 1, mid + 1, end, idx, newVal);
        }
        tree[node] = tree[2 * node] ^ tree[2 * node + 1];
    }

    private int querySegment(int node, int start, int end, int l, int r) {
        if (r < start || end < l) return 0;
        if (l <= start && end <= r) return tree[node];
        int mid = (start + end) / 2;
        return querySegment(2 * node, start, mid, l, r) ^ querySegment(2 * node + 1, mid + 1, end, l, r);
    }

    private int queryPath(int u, int v, int n) {
        int resMask = 0;
        while (head[u] != head[v]) {
            if (depth[head[u]] < depth[head[v]]) {
                int temp = u; u = v; v = temp;
            }
            resMask ^= querySegment(1, 0, n - 1, pos[head[u]], pos[u]);
            u = parent[head[u]];
        }
        if (depth[u] > depth[v]) {
            int temp = u; u = v; v = temp;
        }
        resMask ^= querySegment(1, 0, n - 1, pos[u], pos[v]);
        return resMask;
    }
}