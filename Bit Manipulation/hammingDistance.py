class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

        Given two integers x and y, calculate the Hamming distance.

        Better than 100% of submissions. Not many different ways, not bad.
        Should've done something better than the list comp. Less space?
        """
        diff = x
        diff ^= y
        binDiff = bin(diff)
        diffBits = [ones for ones in binDiff[2:] if ones == "1"]
        return len(diffBits)

        # Better implementation because no list space
        '''
        diff = x^y
        count = 0
        while diff != 0:
            count += diff & 1
            diff >>= 1  # shift to the right one

        return count

        '''
