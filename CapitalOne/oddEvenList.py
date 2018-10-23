# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        Given a singly linked list, group all odd nodes together followed by
        the even nodes. Please note here we are talking about the node number
         and not the value in the nodes.

        You should try to do it in place. The program should run in O(1) space
        complexity and O(nodes) time complexity.
        """
        if not head:
            return None

        oddList = ListNode(0)
        oCurr = oddList
        evenList = ListNode(0)
        eCurr = evenList
        ptr = head
        cnt = 0
        while ptr:
            cnt += 1
            if cnt % 2 == 1:
                oCurr.next = ptr
                oCurr = oCurr.next
            else:
                eCurr.next = ptr
                eCurr = eCurr.next
            ptr = ptr.next
        if eCurr.next:
            eCurr.next = None

        oCurr.next = evenList.next
        return oddList.next


def printList(head):
    while head:
        print(head.val)
        head = head.next


if __name__ == "__main__":
    x = ListNode(1)
    # x.next = ListNode(2)
    # x.next.next = ListNode(3)
    # x.next.next.next = ListNode(4)
    # x.next.next.next.next = ListNode(5)
    run = Solution()
    printList(run.oddEvenList(x))
