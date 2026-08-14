# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0
        
        def height(node):
            if node == None:
                return 0
            
            ld = height(node.left)
            rd = height(node.right)
            
            self.diameter = max(self.diameter, ld + rd)
            
            return 1 + max(ld, rd)
        
        height(root)
        return self.diameter
            
