class Solution:
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in their binary representation and return them as an array.

        Follow up:
        It is very easy to come up with a solution with run time O(n*sizeof(integer)). But can you do it in linear time O(n) /possibly in a single pass?
        Space complexity should be O(n).
        Can you do it like a boss? Do it without using any builtin function like __builtin_popcount in c++ or in any other language.

        Easy Solution:
        """
        arr = []
        for i in range(num + 1):
            count = 0
            while i != 0:
                count += i & 1
                i >>= 1
            arr.append(count)
        return arr

        # Better Solution:
        ans = [0] * (num + 1)
        for i in range(1, num + 1):
            ans[i] = ans[i // 2] + (i % 2)
        return ans

        # Another:
        lst = [0]
        while len(lst) <= num:
            lst += [i + 1 for i in lst]
        return lst[:num + 1]
