
class TicTacToe(object):

    def __init__(self, n):
        self.n = n
        self.rows = [0] * n
        self.colums = [0] * n
        self.diag = [0, 0]  # diag[0] is total value of left -> right diagonal, diag[1] is total value of right -> left diagonal

    def move(self, row, col, player):
        value = (1.5 - player) * 2
        self.rows[row] += value
        self.colums[col] += value
        if row == col:
            self.diag[0] += value
        if row + col == self.n - 1:
            self.diag[1] += value
        if abs(self.rows[row]) == self.n or abs(self.colums[col]) == self.n or abs(self.diag[0]) == self.n or abs(self.diag[1]) == self.n:  # win is either a total value of all 1s or all -1s
            return player
        return 0
