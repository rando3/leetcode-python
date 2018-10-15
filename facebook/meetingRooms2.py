# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        start = sorted([i.start for i in intervals])  # O(nlogn)
        end = sorted([i.end for i in intervals])

        si = ei = room = 0  # e as a pointer to first avail room
        while si < len(start):
            if start[si] < end[ei]:
                room += 1
            else:
                ei += 1
            si += 1
        return room


class Solution2(object):
    def minMeetingRooms(self, intervals):
        starts = sorted(i.start for i in intervals)
        ends = sorted(i.end for i in intervals)

        e = 0
        numRooms = available = 0
        for start in starts:
            while ends[e] <= start:
                available += 1
                e += 1
            if available:
                available -= 1
            else:
                numRooms += 1

        return numRooms
