#! /bin/python
from board import *
from tree import *
import utils


def build_tree(root, level):
    root.data.level = level
    winner = root.data.getWinner()
    if winner != 0:
        root.data.winner = winner
        if winner == 1:
            root.data.winway = 1
            root.data.win += 1
        else:
            root.data.lose += 1

        root.data.game += 1
        root.data.ratio = root.data.win / root.data.game
        return

    elif level == 9:
        root.data.tie += 1
        root.data.game += 1
        root.data.ratio = root.data.win / root.data.game
        return

    player = level % 2 + 1
    for row in range(3):
        for col in range(3):
            if root.data.mat[row][col] == 0:
                son = Node(root, [], Board())
                root.sons.append(son)
                son.data.copy(root.data)
                son.data.put(player, row, col)
                build_tree(son, level + 1)


    oddLevel = level%2
    root.data.winway = oddLevel
    for son in root.sons:
        if oddLevel != son.data.winway:
            root.data.winway = son.data.winway

        root.data.win += son.data.win
        root.data.lose += son.data.lose
        root.data.tie += son.data.tie
        root.data.game += son.data.game
        if son.data.winway == 1:
            root.data.debug += 1
    root.data.debug /= len(root.sons)
    root.data.ratio = root.data.win / root.data.game
    root.data.level = level

option_str = ''
while(option_str != 'q'):
    print('\033c')

    print("Building tree.")
    tree = Tree(Board(), build_tree, 0)

    currentNode = tree.root
    currentNode.print()

    while (option_str != 'q'):
        if(option_str == ''):
            option_str = input("Type h for help: ")
        else:
            option_str = input()

        if option_str == 'h':
            utils.printHelp()
            input("\nPress Enter to leave.")
            currentNode.print()
        elif option_str == 'r':
            break

        #Node jumping
        try:
            option = int(option_str)
        except ValueError:
            continue
        if 0 < option <= len(currentNode.sons):
            currentNode = currentNode.sons[option-1]
        elif option == 0 and currentNode.parent != None:
            currentNode = currentNode.parent
        ###############

        currentNode.print()

print('\033c')
print("Leaving...")
