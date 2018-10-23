import heapq


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return str(self.val)


class Solution(object):

    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        O(kn*log(k))
        """
        if not lists:
            return None
        minheap = [(l.val, l) for l in lists if l]
        heapq.heapify(minheap)

        head = ListNode(0)
        curr = head

        while minheap:
            popped = heapq.heappop(minheap)
            curr.next = popped[1]
            curr = curr.next
            if curr.next:
                heapq.heappush(minheap, (curr.next.val, curr.next))
        return head.next


def mergeLists(lists):
    '''
    Just sorting list before making a linked list
    O(kn*log(kn)
    '''
    nodes = []
    merged = ListNode(0)
    curr = merged

    for l in lists:
        while l:
            nodes.append(l.val)
            l = l.next
    nodes.sort()

    for x in nodes:
        curr.next = ListNode(x)
        curr = curr.next

    return merged.next


def printList(head):
    while head:
        print(head.val)
        head = head.next

if __name__ == "__main__":
    run = Solution()
    head1 = ListNode(1)
    head1.next = ListNode(4)
    head1.next.next = ListNode(7)
    head2 = ListNode(3)
    head2.next = ListNode(4)
    head2.next.next = ListNode(6)
    head3 = ListNode(0)
    head3.next = ListNode(1)
    head3.next.next = ListNode(5)
    printList(run.mergeKLists([head1, head2, head3]))
