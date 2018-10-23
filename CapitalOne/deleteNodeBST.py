class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if not root:
            return root

        if root.val == key:
            left, right = root.left, root.right
            if left:  # put root.right to the right of farthest right in left
                root = p = left
                while p.right:
                    p = p.right
                p.right = right
            else:
                root = right
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            root.right = self.deleteNode(root.right, key)
        return root
