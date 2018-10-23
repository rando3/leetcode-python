# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        Iterate through two linkedlists and do place based addition with a carry. Will be in reverse order (to make carrying a bit easier)
        """
        head = ListNode(0)
        curr = head
        carry = 0

        while l1.next or l2.next or carry:
            summed = -1
            if l1.val:
                add1 = l1.val
                summed = add1
            if l2.val:
                add2 = l2.val
                if summed != -1:
                    summed += add2
                else:
                    summed = add2
            if summed == -1 and carry:
                summed = carry
            else:
                summed += carry
            rem = summed % 10
            print(rem)
            carry = summed // 10
            curr.next = ListNode(rem)
            curr = curr.next
            if l1.next:
                l1 = l1.next
            if l2.next:
                l2 = l2.next

        return head.next
