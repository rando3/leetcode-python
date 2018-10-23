# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def addTwoNumbers(l1, l2):
    '''Iterate through two linkedlists and do place based addition with a carry. Will be in reverse order (to make carrying a bit easier)'''
    head = ListNode(0)
    curr = head
    carry = 0
    while l1 or l2 or carry:
        if l1 and l2:
            tempSum = l1.val
            tempSum += l2.val
            tempSum += carry
            carry = tempSum // 10
            summed = tempSum % 10
            curr.next = ListNode(summed)
            l1 = l1.next
            l2 = l2.next
            curr = curr.next
        elif l1:
            tempSum = l1.val
            tempSum += carry
            summed = tempSum % 10
            carry = tempSum // 10
            curr.next = ListNode(summed)
            l1 = l1.next
            curr = curr.next
        elif l2:
            tempSum = l2.val
            tempSum += carry
            summed = tempSum % 10
            carry = tempSum // 10
            curr.next = ListNode(summed)
            curr = curr.next
            l2 = l2.next
        elif carry:
            # print(carry)
            curr.next = ListNode(carry)
            curr = curr.next
            carry = 0
    return head.next


def addNumbers(self, l1, l2):
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


def printList(head):
    while head:
        print(head.val)
        head = head.next


if __name__ == "__main__":
    l1 = ListNode(6)
    # l1.next = ListNode(9)
    # l1.next.next = ListNode(1)
    l2 = ListNode(4)
    # l2.next = ListNode(5)
    # l2.next.next = ListNode(4)

    printList(addTwoNumbers(l1, l2))
