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
    print("COMMANDS:")
    print("----------------------------------------------------------")
    print('{:>10}'.format("h:"), '{:>40}'.format("help"))
    print('{:>10}'.format("[0-9]:"), '{:>40}'.format("nodes navigation"))
    print('{:>10}'.format("r:"), '{:>40}'.format("restart"))
    print('{:>10}'.format("q:"), '{:>40}'.format("quit"))
    print("SYMBOLS:")
    print("----------------------------------------------------------")
    print('{:>10}'.format("win:"), '{:>40}'.format("no. of wins in subtree"))
    print('{:>10}'.format("lose:"), '{:>40}'.format("no. of loses in subtree"))
    print('{:>10}'.format("tie:"), '{:>40}'.format("no. of ties in subtree"))
    print('{:>10}'.format("game:"), '{:>40}'.format("no. of games in subtree"))
    print('{:>10}'.format("ratio:"), '{:>40}'.format("win/game ratio"))
    print('{:>10}'.format("winner:"), '{:>40}'.format("winner of board"))

