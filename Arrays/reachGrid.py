class Solution:
    # @param X : list of integers
    # @param Y : list of integers
    # Points are represented by (X[i], Y[i])
    # @return an integer
    '''
    You are in an infinite 2D grid where you can move in any of the 8 directions
    You are given a sequence of points and the order in which you need to cover the points.
    Give the minimum number of steps in which you can achieve it. You start from the first point.
    Input : [(0, 0), (1, 1), (1, 2)]
    Output : 2
    '''
    def coverPoints(self, X, Y):
        steps = 0
        for i in range(0, len(X) - 1):
            steps += max(abs(X[i + 1] - X[i]), abs(Y[i + 1] - Y[i]))
        return steps
