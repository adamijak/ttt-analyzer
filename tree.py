class Tree:
    def __init__(self, root_data, func, *args):
        self.root = Node(data = root_data)
        func(self.root, *args)

class Node:
    def __init__(self, parent=None, sons=[], data=None):
        self.parent = parent
        self.sons = sons
        self.data = data

    def print(self):
        print('\033cCurrent node:')
        print("--------------------------------------------------------------------")
        self.data.print()

        print("Current node sons:")
        print("--------------------------------------------------------------------")
        print("0: Parent\n")
        for son_idx in range(len(self.sons)):
            print(son_idx + 1, ":", sep='')
            self.sons[son_idx].data.print()
