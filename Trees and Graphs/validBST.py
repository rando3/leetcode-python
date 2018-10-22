# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        path = []

        def inorder(root):
            if root:
                inorder(root.left)
                path.append(root.val)
                inorder(root.right)
        inorder(root)
        return all(path[i] < path[i+1] for i in range(len(path) - 1))
