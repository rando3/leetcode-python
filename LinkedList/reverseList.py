# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode

        Accepted: Beats 70%
        """
        if head.val is None:
            return None
        q = []
        while head is not None:
            q.append(head.val)
            head = head.next
        newL = ListNode(q.pop())
        n = newL
        while q:
            n.next = ListNode(q.pop())
            n = n.next
        n.next = None
        return newL

        '''Better iterative solution'''
        prev = None
        while head:
            curr = head
            head = head.next
            curr.next = prev
            prev = curr
        return prev


if __name__ == '__main__':
    use = Solution()
    test = ListNode(1)
    first = test
    test.next = ListNode(2)
    test = test.next
    test.next = ListNode(3)
    test = test.next
    test.next = ListNode(4)
    test = test.next
    test.next = ListNode(5)
    test = test.next
    test.next = None
    linkedList = use.reverseList(first)
    while linkedList is not None:
        print(linkedList.val)
        linkedList = linkedList.next
