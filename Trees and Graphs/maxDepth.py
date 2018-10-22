# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        Find max depth of binary tree
        Beats 75% of submissions. Recursive
        """
        if root is None:
            return 0
        else:
            maxL = self.maxDepth(root.left)
            maxR = self.maxDepth(root.right)
            if (maxL > maxR):
                return maxL + 1
            else:
                return maxR + 1

        '''
        Iterative below
        '''
        '''
        if root is None:
            return 0
        tmp=[root]
        depth=0
        while tmp:
            temp=[]
            depth+=1
            for i in tmp:
                if i.left:
                    temp.append(i.left)
                if i.right:
                    temp.append(i.right)
            if temp==[]:
                return depth
            else:
                tmp=temp
        '''
