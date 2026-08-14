class Solution:
    def countNodes(self, root):
        
        def getLeftHeight(node):
            height = 0
            while node:
                height += 1
                node = node.left
            return height
        
        def getRightHeight(node):
            height = 0
            while node:
                height += 1
                node = node.right
            return height
        
        if not root:
            return 0
        
        left_h = getLeftHeight(root)
        right_h = getRightHeight(root)
        
        # If perfect tree
        if left_h == right_h:
            return (1 << left_h) - 1
        
        # Otherwise recurse
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)