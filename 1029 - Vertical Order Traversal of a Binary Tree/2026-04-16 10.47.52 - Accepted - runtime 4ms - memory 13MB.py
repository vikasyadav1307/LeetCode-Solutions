from collections import defaultdict

class Solution:
    def verticalTraversal(self, root):
        nodes = defaultdict(list)
        
        def dfs(node, row, col):
            if not node:
                return
            
            nodes[col].append((row, node.val))
            
            dfs(node.left, row + 1, col - 1)
            dfs(node.right, row + 1, col + 1)
        
        dfs(root, 0, 0)
        
        result = []
        
        for col in sorted(nodes.keys()):
            # sort by row first, then value
            column = sorted(nodes[col])
            result.append([val for row, val in column])
        
        return result