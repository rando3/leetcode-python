from heapq import heappop, heappush


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):

    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        h = []
        c = 0 # counter to avoid tie
        dummy = cur = ListNode(1)
        for head in lists:
            if head:
                heappush(h, (head.val, c, head))
                c += 1

        while h:
            v, d, node = heappop(h)
            #we are not using d
            cur.next = node
            cur = cur.next
            if node.next:
                c += 1
                heappush(h, (node.next.val, c, node.next))

        return dummy.next
