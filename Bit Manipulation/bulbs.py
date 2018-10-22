class Solution:
    # @param A : list of integers
    # @return an integer

    '''
    Facebook Codelab
    No hints or solutions needed
    '''
    def bulbs(self, A):
        if A is None:
            return None
        if len(A) == 0:
            return 0

        cnt = 0
        rightFlipped = False
        for i, v in enumerate(A):
            if v ^ rightFlipped:
                continue
            else:
                A[i] = 1
                cnt += 1
                rightFlipped = not rightFlipped
        return cnt


if __name__ == "__main__":
    A = [3, 0, 1, 0]
