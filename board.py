import copy

class Board:
    val_strings = ["win: ", "lose: ", "tie: ", "game: ", "ratio: ", "winner: ", "winway: ", "level: ", "debug: "]
    def __init__(self):
        self.ratio = 0.
        self.win = 0
        self.lose = 0
        self.tie = 0
        self.game = 0
        self.winner = 0
        self.mat = None
        self.winway = 0
        self.level = 0
        self.debug = 0
        self.reset()

    #reset board to 0
    def reset(self):
        self.mat = [[0]*3 for i in range(3)]

    #put stone on board
    def put(self, stone, row, col):
        if self.mat[row][col] != 0:
            return False
        self.mat[row][col] = stone
        return True

    #copy gamestate from other board
    def copy(self, other):
        self.mat = copy.deepcopy(other.mat)

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
        values = [self.win, self.lose, self.tie, self.game, self.ratio, self.winner, self.winway, self.level, self.debug]
        strings = []
        for value,string in zip(values,self.val_strings):
            strings.append('{:>10}{:<10}'.format(string,round(value,5)))
        strings = iter(strings)

        for _ in range(3):
            print(next(mat_iter),end = " ")
            for _ in range(3):
                print(next(strings, "                    "), " | ", end="")
            print()
