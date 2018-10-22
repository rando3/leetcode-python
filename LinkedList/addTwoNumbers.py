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
        """
        addition = ListNode(None)
        ptr = addition
        curr1 = l1
        curr2 = l2
        carry = 0

        while curr1.next or curr2.next or carry:
            summed = -1
            if curr1.val:
                add1 = curr1.val
                summed = add1
            if curr2.val:
                add2 = curr2.val
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
            ptr.next = ListNode(rem)
            ptr = ptr.next
            if curr1.next:
                curr1 = curr1.next
            if curr2.next:
                curr2 = curr2.next

        return addition.next
