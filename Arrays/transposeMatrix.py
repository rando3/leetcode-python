class Solution:
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        Given a matrix A, return the transpose of A.

        The transpose of a matrix is the matrix flipped over it's main diagonal, switching the row and column indices of the matrix.

        """
        transposed = []
        for i in range(len(A[0])):
            transposeList = []
            for list in A:
                transposeList.append(list[i])
            transposed.append(transposeList)
        return transposed
