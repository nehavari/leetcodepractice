'''
Morris post order traversal
'''
class Solution:          
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = deque()
        while root:
            if root.right:
                print("root.right", root.right.val)
                temp = root.right
                while temp.left and temp.left != root:
                    temp = temp.left
                if not temp.left:
                    print("********", root.val, "********")
                    res.appendleft(root.val)
                    temp.left = root
                    root = root.right
                else:
                    temp.left = None
                    root = root.left
            else:
                print("*****in else********", root.val)
                res.appendleft(root.val)
                if root.left:
                    print("root.left", root.left.val)
                else:
                    print("root.left is None")
                root = root.left
                
        return res