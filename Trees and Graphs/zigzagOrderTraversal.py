from collections import deque
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        res = []
        temp = []
        q = deque()
        q.append(root)
        flag = 1

        while q:
            # print([x.val for x in q])
            for i in range(len(q)):
                node = q.popleft()
                temp.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(temp[::flag])
            temp = []
            flag *= -1
        return res


if __name__ == "__main__":
    run = Solution()
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.left.left = TreeNode(14)
    root.left.right = TreeNode(19)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print(run.zigzagLevelOrder(root))

