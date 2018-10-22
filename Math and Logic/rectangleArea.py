class Solution:
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        len1 = C - A
        wid1 = D-B
        len2 = G-E
        wid2 = H-F
        area1 = len1 * wid1
        area2 = len2 * wid2
        overx = 0
        overy = 0
        range2 = set(range(E,G))
        inter = range2.intersection(range(A,C))
        overx = len(inter)
        range2 = set(range(F,H))
        inter = range2.intersection(range(B,D))
        overy = len(inter)
        return (area1 + area2 - (overx*overy))