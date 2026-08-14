# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root, key):
        if not root:
            return None
        
        # Step 1: Search node
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        
        else:
            # Node found
            
            # Case 1: No child
            if not root.left and not root.right:
                return None
            
            # Case 2: One child
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            
            # Case 3: Two children
            # Find inorder successor (smallest in right subtree)
            successor = root.right
            while successor.left:
                successor = successor.left
            
            # Replace value
            root.val = successor.val
            
            # Delete successor
            root.right = self.deleteNode(root.right, successor.val)
        
        return root