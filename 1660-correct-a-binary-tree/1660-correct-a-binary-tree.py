# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def correctBinaryTree(self, root: TreeNode) -> TreeNode:
        queue = deque([(root, None)])
        seen = set()
        
        while queue:
            for _ in range(len(queue)):
                node, parent = queue.popleft()
                seen.add(node.val)
                if node.right:
                    if node.right.val in seen:
                        if parent.right == node:
                            parent.right = None
                        else:
                            parent.left = None
                    else:
                        queue.append((node.right, node))
                if node.left:
                    queue.append((node.left, node))
        
        return root