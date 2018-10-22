# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode(-1)
        curr = head

        while l1 or l2:
            if not l1:
                curr.next = l2
                l2 = l2.next
            elif not l2:
                curr.next = l1
                l1 = l1.next
            elif l1.val > l2.val:
                curr.next = l2
                l2 = l2.next
            elif l2.val >= l1.val:
                curr.next = l1
                l1 = l1.next
            curr = curr.next
        return head.next


if __name__ == "__main__":
    x = ListNode(1)
    x.next = ListNode(2)
    x.next.next = ListNode(4)
    y = ListNode(1)
    y.next = ListNode(3)
    y.next.next = ListNode(4)
    run = Solution()
    run.mergeTwoLists(x, y)