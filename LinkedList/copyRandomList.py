# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

        Return a deep copy of the list.

        Easiest thing to do is put new ListNodes into a dictionary (using a head pointer, then use another head pointer to) set the nexts and randoms of each node by getting (labels) from the dict using the pointer's .next and .random

        Return head node from dict
        """
        d = {}
        l = m = head
        while l:
            d[l] = RandomListNode(l.label)
            l = l.next
        while m:
            d[m].next = d.get(m.next)
            d[m].random = d.get(m.random)
            m = m.next
        return d.get(head)
