from collections import defaultdict, deque

class Triplet:
    def __init__(self, node, x, y):
        self.node = node
        self.x = x  # row
        self.y = y  # column

class Solution:
    def verticalTraversal(self, root):
        ans = defaultdict(list)
        q = deque([Triplet(root, 0, 0)])
        
        while q:
            temp = defaultdict(list)
            
            for _ in range(len(q)):
                t = q.popleft()
                node, x, y = t.node, t.x, t.y
                
                # store (row, value)
                temp[y].append((x, node.val))
                
                if node.left:
                    q.append(Triplet(node.left, x+1, y-1))
                if node.right:
                    q.append(Triplet(node.right, x+1, y+1))
            
            # sort by row, then value
            for col in temp:
                temp[col].sort()
                for x, val in temp[col]:
                    ans[col].append(val)
        
        # build result
        result = []
        for col in sorted(ans.keys()):
            result.append(ans[col])
        
        return result