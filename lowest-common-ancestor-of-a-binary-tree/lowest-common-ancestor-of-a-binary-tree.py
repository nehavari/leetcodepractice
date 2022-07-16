# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
Iterative approach of finding lowestCommonAncestor.
leetcode has 3 solutions for it, this is the 4th way of solving this.
O(n)
O(n)
'''

class Solution:
        
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        stack = [] 
        parent = found = prev = None
        while root or stack:
            if root:
                while root:
                    prev = root
                    if root == p or root == q:
                        if not found:
                            found = p if root == p else q
                            parent = prev
                        else:
                            return found
                    stack.append(root)   
                    root = root.left
            root = stack.pop()
            if  root == parent:
                found = parent
                if stack:
                    parent = stack[-1]
            root = root.right
                
        return None