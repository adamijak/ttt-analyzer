import pickle

def load_object(filename):
    with open(filename, 'rb') as fd:
        return pickle.load(fd)
def save_object(obj, filename):
    with open(filename, 'wb') as output:  # Overwrites any existing file.
        pickle.dump(obj, output, pickle.HIGHEST_PROTOCOL)

def printHelp():
    print('\033cHELP')
    print("----------------------------------------------------------")
    print("This is help for TicTacToe analyzer.\n")
    print("KEYS:")
    print("----------------------------------------------------------")
    print('{:>10}'.format("h:"), '{:>20}'.format("help"))
    print('{:>10}'.format("[0-9]:"), '{:>20}'.format("nodes navigation"))
    print('{:>10}'.format("r:"), '{:>20}'.format("restart"))
    print('{:>10}'.format("q:"), '{:>20}'.format("quit"))
    print("SYMBOLS:")
    print("----------------------------------------------------------")
    print('{:>10}'.format("win:"), '{:>20}'.format("no. of wins in subtree"))
    print('{:>10}'.format("lose:"), '{:>20}'.format("no. of loses in subtree"))
    print('{:>10}'.format("tie:"), '{:>20}'.format("no. of ties in subtree"))
    print('{:>10}'.format("game:"), '{:>20}'.format("no. of games in subtree"))
    print('{:>10}'.format("ratio:"), '{:>20}'.format("win/game ratio"))
    print('{:>10}'.format("winner:"), '{:>20}'.format("winner of board"))

