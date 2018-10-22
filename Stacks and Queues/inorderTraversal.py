# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    # def nodesToList(self, inorder):
    #     r = []
    #     for x in inorder:
    #         r.append(x.val)
    #     return str(r)

    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        Given a binary tree, return the inorder traversal of its nodes' values.
        Follow up: Recursive solution is trivial, could you do it iteratively?
        Medium
        Check for 'in' doesn't work, infinite loop :(
        """

    '''Recursive '''
    def inorderTraversal2(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.path = []  # if declared outside methods -- residual values remain!!
        self.inorder(root)
        return self.path

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            self.path.append(root.val)
            self.inorder(root.right)

    ''' MIND BLOWING solution: '''
    # Use a tuple with a boolean to check for visited, DUH!
    def inorder2(self, root):
        result, stack = [], [(root, False)]
        while stack:
            root, is_visited = stack.pop()
            if root is None:
                continue
            if is_visited:
                result.append(root.val)
            else:
                stack.append((root.right, False))
                stack.append((root, True))
                stack.append((root.left, False))
        return result

    def inorder3(self, root):
        ''' Great solution, no boolean '''
        result, stack = [], []
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                temp = stack.pop()
                result.append(temp.val)
                root = temp.right
        return result


if __name__ == '__main__':
    sol = Solution()
    t = TreeNode(1)
    t.right = TreeNode(2)
    t.right.left = TreeNode(3)
    print(sol.inorderTraversal(t))
