class ListNode:
    def __init__(self, data=None):
        self.val = data
        self.next = None


class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def deleteDuplicates(self, A):
        head = A
        if A is None or A.next is None:
            return head

        while A:
            if A.next and A.val == A.next.val:
                A.next = A.next.next
                continue  # have to compare next to A, so don't update A yet
            A = A.next
        return head
