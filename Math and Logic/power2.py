import math


class Solution:
    # @param A : integer
    # @return a boolean
    '''
    Check if integer can be made a power of A^P where A > 0 and P > 1
    '''
    def isPower(self, N):
        if N == 0:
            return False
        if N == 1:
            return True
        for p in range(2, 33):
            for A in range(2, int(N**(1.0 / p)) + 2):
                if A**p == N:
                    return True
        return False

    # or

    def isPower2(self, A):
        if A == 1:  # 1^ anything
            return True
        for j in range(2, int(math.sqrt(A)) + 1):
            i = A
            while (i % j == 0):
                i = i // j
            if i == 1:
                return True
        return False
