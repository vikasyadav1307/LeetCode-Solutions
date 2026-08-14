from collections import deque

class Solution:
    def zigzagLevelOrder(self, root):
        if not root:
            return []
        
        res = []
        q = deque([root])
        left = True
        
        while q:
            level = deque()
            
            for _ in range(len(q)):
                node = q.popleft()
                
                if left:
                    level.append(node.val)
                else:
                    level.appendleft(node.val)
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            res.append(list(level))
            left = not left
        
        return res