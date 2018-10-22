class Solution:
    # @param A : list of integers
    # @return an integer

    '''
    Facebook Codelab
    No hints or solutions needed

    N light bulbs are connected by a wire. Each bulb has a switch associated with it, however due to faulty wiring, a switch also changes the state of all the bulbs to the right of current bulb. Given an initial state of all bulbs, find the minimum number of switches you have to press to turn on all the bulbs. You can press the same switch multiple times.
    Input : [0 1 0 1]
    Return : 4
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
