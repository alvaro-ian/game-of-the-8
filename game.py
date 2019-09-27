end_table = [[1, 2, 3], [4, 5, 6], [7, 8, 'b']]
move_directions = {'UP': 0, 'RIGHT': 1, 'DOWN': 2, 'LEFT': 3}
# Indexes of the tuple for the position of the 'b' tile
line = 0
column = 1

class Game8:
    def __init__(self, table):
        self.table = table
        self.moves = 0
        self.b_position = self.get_b_position()

    def check_win(self):
        if self.table == end_table:
            return True
        return False

    # Function for movement of the 'b' tile, returns False if the movement can't occur
    def move(self, direction):
        # Moving 'b' up
        if direction == move_directions['UP']:
            # Can't move up on first line
            if self.b_position[line] == 0:
                return False
            aux = self.table[self.b_position[line] - 1][self.b_position[column]]
            self.table[self.b_position[line] - 1][self.b_position[column]] = 'b'
            self.table[self.b_position[line]][self.b_position[column]] = aux
        # Moving 'b' right
        if direction == move_directions['RIGHT']:
            # Can't move right on last column
            if self.b_position[column] == 2:
                return False
            aux = self.table[self.b_position[line]][self.b_position[column] + 1]
            self.table[self.b_position[line]][self.b_position[column] + 1] = 'b'
            self.table[self.b_position[line]][self.b_position[column]] = aux
        # Moving 'b' down
        if direction == move_directions['DOWN']:
            # Can't move down on last line
            if self.b_position[line] == 2:
                return False
            aux = self.table[self.b_position[line] + 1][self.b_position[column]]
            self.table[self.b_position[line] + 1][self.b_position[column]] = 'b'
            self.table[self.b_position[line]][self.b_position[column]] = aux
        # Moving 'b' left
        if direction == move_directions['LEFT']:
            # Can't move left on first column:
            if self.b_position[column] == 0:
                return False
            aux = self.table[self.b_position[line]][self.b_position[column] - 1]
            self.table[self.b_position[line]][self.b_position[column] - 1] = 'b'
            self.table[self.b_position[line]][self.b_position[column]] = aux
        # Updates 'b' position
        self.b_position = self.get_b_position()
        self.moves += 1
        return True
            
    def get_b_position(self):
        for i in range(len(self.table)):
            for j in range(len(self.table[i])):
                if self.table[i][j] == 'b':
                    return (i, j)

    def show_table(self):
        print('----------------')
        for i in range(len(self.table)):
            for j in range(len(self.table[i])):
                print(str(self.table[i][j]), end = ' ')
            print()
        print('----------------')