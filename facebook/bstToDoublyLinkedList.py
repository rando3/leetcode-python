# Definition for a Node.
class Node(object):
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def treeToDoublyList(self, root):
        """
        :type root: Node
        :rtype: Node
        Convert a BST to a sorted circular doubly-linked list in-place. Think of the left and right pointers as synonymous to the previous and next pointers in a doubly-linked list.

        Let's take the following BST as an example, it may help you understand the problem better:
        We want to transform this BST into a circular doubly linked list. Each node in a doubly linked list has a predecessor and successor. For a circular doubly linked list, the predecessor of the first element is the last element, and the successor of the last element is the first element.

        The figure below shows the circular doubly linked list for the BST above. The "head" symbol means the node it points to is the smallest element of the linked list.

        """

        def helper(curr):
            head, tail = curr, curr
            if curr.left:
                lhead, ltail = helper(curr.left)
                ltail.right = curr
                curr.left = ltail
                head = lhead
            if curr.right:
                rhead, rtail = helper(curr.right)
                rhead.left = curr
                curr.right = rhead
                tail = rtail
            return head, tail

        if root:
            head, tail = helper(root)
            head.left = tail
            tail.right = head
            return head
        else:
            return None

    def treeToDoublyList2(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        def traverse(node):
            if not node.left and not node.right:
                return node, node
            if node.left:
                hl, tl = traverse(node.left)
                tl.right = node
                node.left = tl
            else:
                hl, tl = node, node
            if node.right:
                hr, tr = traverse(node.right)
                hr.left = node
                node.right = hr
            else:
                hr, tr = node, node
            return hl, tr

        if not root:
            return None
        hl, tr = traverse(root)
        hl.left = tr
        tr.right = hl
        return hl
