# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
O(n) -- time complexity
O(n) -- space complexity
"""
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        output = []
        while root:
            output.append(root.val)
            if root.left:
                if root.right:
                    node = root.left
                    while node.right:
                        node = node.right
                    node.right = root.right
                root = root.left
            elif root.right:
                root = root.right
            else:
                root = None
        
        return output