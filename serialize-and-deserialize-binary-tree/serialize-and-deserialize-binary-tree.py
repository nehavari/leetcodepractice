# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
"""
Iterative approach based of Level Order Traversal of tree
Leetcode solutions have only recursive approach
"""
from collections import deque
class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ''
        queue = deque()
        queue.appendleft(root)
        ser = []
        while queue:
            size = len(queue)
            for index in range(size):
                node = queue.pop()
                if node:
                    ser.append(str(node.val))
                else:
                    ser.append('null')
                    continue
                
                if node.left:
                    queue.appendleft(node.left)
                else:
                    queue.appendleft(None)
                    
                if node.right:
                    queue.appendleft(node.right)
                else:
                    queue.appendleft(None)
        return ','.join(ser)
                    
                    

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return []
        
        deser = data.split(',')
        queue = deque()
        prev = root = None
        for element in deser:
            node = TreeNode(int(element)) if element != 'null' else None
            if not root:
                root = node
            if queue or prev:
                if not prev:
                    parent = queue.pop()
                    while not parent:
                        parent = queue.pop()
                    parent.left = node
                    prev = parent
                else:
                    prev.right = node
                    prev = None
            queue.appendleft(node)
        return root
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))