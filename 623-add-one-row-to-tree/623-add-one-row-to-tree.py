# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque 
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if not root:
            return root
        if depth == 1:
            new_root = TreeNode(val)
            new_root.left = root
            return new_root
        save_root = root
        queue = deque()
        queue.append((root, 1))
        while queue:            
            root, curr_depth = queue.popleft()
            if curr_depth == depth - 1:
                left, right = root.left, root.right
                left_node, right_node = TreeNode(val), TreeNode(val)
                root.left, root.right = left_node, right_node
                left_node.left, right_node.right = left, right
            else:
                if root.left:
                    queue.append((root.left, curr_depth + 1))
                if root.right:
                    queue.append((root.right, curr_depth + 1))
                
        return save_root
                
                
                
            