class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        Given a binary matrix A, we want to flip the image horizontally, then invert it, and return the resulting image.

        To flip an image horizontally means that each row of the image is reversed.  For example, flipping [1, 1, 0] horizontally results in [0, 1, 1].

        To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0. For example, inverting [0, 1, 1] results in [1, 0, 0].
        """
        invertedList = []
        reversedList = [v[::-1] for i, v in enumerate(A)]
        for arr in reversedList:
            invArr = []
            for i in range(len(arr)):
                if arr[i] == 1:
                    invArr.append(0)
                else:
                    invArr.append(1)
            invertedList.append(invArr)
        return invertedList
