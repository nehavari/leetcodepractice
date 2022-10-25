# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.prev = -math.inf
        
        def inorder(root):
            if root:
                if not inorder(root.left):
                    return False
                if self.prev >= root.val:
                    return False
                self.prev = root.val
                return inorder(root.right)
            return True
            
        return inorder(root)
            
                
        
        