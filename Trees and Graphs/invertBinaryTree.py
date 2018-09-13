# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        Invert a binary tree.
        FIRST PROBLEM WHERE I GOT THE SOLUTION AFTER ONE GO OF USING THE CTCI METHOD!!!!!!!!!!!!!!!!!!!!!
        :) :) :) :)
        Beats 99% of solutions.
        """
        if root is None:
            return None
        if root.left is None and root.right is None:
            return root
        t = root
        left = t.left
        t.left = t.right
        t.right = left

        t.left = self.invertTree(t.left)
        t.right = self.invertTree(t.right)
        return t

        ''' Also, but above is great '''
        if root:
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root
