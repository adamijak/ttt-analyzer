class Board:
    def __init__(self):
        self.ratio = 0.
        self.win = 0
        self.lose = 0
        self.tie = 0
        self.game = 0
        self.winner = 0
        self.mat = None
        self.reset()

    #reset board to 0
    def reset(self):
        if self.mat == None:
            self.mat = [[0]*3 for i in range(3)]
        else:
            for row in range(3):
                for col in range(3):
                    self.mat[row][col] = 0

    #put stone on board
    def put(self, stone, row, col):
        if self.mat[row][col] != 0:
            return False
        if stone != 1 and stone != 2:
            return False
        if row < 0 or 3 <= row:
            return False
        if col < 0 or 3 <= col:
            return False

        self.mat[row][col] = stone
        return True

    #copy gamestate from other board
    def copy(self, other):
        for row in range(3):
            for col in range(3):
                self.mat[row][col] = other.mat[row][col]

    #return winner of board. If no winer return 0
    def getWinner(self):
        mat = self.mat
        for i in range(3):
            if (mat[i][0] == mat[i][1] == mat[i][2] != 0) or (mat[0][i] == mat[1][i] == mat[2][i] != 0):
                return mat[i][i]
        if (mat[0][0] == mat[1][1] == mat[2][2] != 0) or (mat[0][2] == mat[1][1] == mat[2][0] != 0):
            return mat[1][1]
        return 0

    def print(self):
        mat_iter = iter(self.mat)
        win_str = '{:>8}'.format('win: ') + '{:<10}'.format(self.win)
        lose_str = '{:>8}'.format('lose: ') + '{:<10}'.format(self.lose)
        tie_str = '{:>8}'.format('tie: ') + '{:<10}'.format(self.tie)
        game_str = '{:>8}'.format('game: ') + '{:<10}'.format(self.game)
        ratio_str = '{:>8}'.format('ratio: ') + '{:<10}'.format(self.ratio)
        winner_str = '{:>8}'.format('winner: ') + '{:<10}'.format(self.winner)
        print((next(mat_iter)), win_str, game_str, sep=' | ')
        print((next(mat_iter)), lose_str, ratio_str, sep=' | ')
        print((next(mat_iter)), tie_str, winner_str, sep=' | ')
