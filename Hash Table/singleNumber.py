class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        Given a non-empty array of integers, every element appears twice except for one. Find that single one.

        Note:

        Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
        Bitwise XOR:
        >>> # this example swaps integers without a temporary variable using XOR
        >>> a = 2
        >>> b = 8
        >>> a ^= b
        >>> b ^= a
        >>> a ^= b
        >>> a
        8
        >>> b
        2
        Just know that when you xor the same thing twice
        it goes back to the orig number:
        A = 4
        B= 7
        A ^= B  # A = (4 ^ 7)
        A ^= B  # A = (A ^ 7)
        A = 4
        """

        # Used a dictionary here, couldn't find a O(N) way without extra space
        # Beats 10% of solutions, there were way worse because
        # they were O(N^2)
        numCount = {}
        for i, x in enumerate(nums):
            if x not in numCount:
                numCount[x] = 1
            else:
                numCount.pop(x, None)
        for key in numCount:
            return key

        '''
        Elegant fast solution:

        a = 0
        for i in nums:
            a ^= i
        return a
        '''
        '''
        Another:

        result = 0
        for num in nums:
            result = result ^ num
        return result
        '''


if __name__ == '__main__':
    sol = Solution()
    sol.singleNumber([4, 1, 2, 1, 2])
