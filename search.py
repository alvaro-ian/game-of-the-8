import game as g
import copy

class StateNode:
    def __init__(self, game: g.Game8, parent, generator, depth, cost):
        self.game = game
        self.parent = parent
        self.generator = generator
        self.depth = depth
        self.cost = cost
        self.sons = []

    # Generates a son node of the current state node based on an operation (in the case of the game movement in four possible directions)
    def generate_son(self, operator):
        son_game = copy.deepcopy(self.game)
        # If the move can't be done returns None
        if not son_game.move(operator):
            return None
        son = StateNode(son_game, self, operator, self.depth + 1, self.cost + 1)
        self.sons.append(son)
        return son

    def toString(self):
        return "Generator: " + str(self.generator) + ", Depth: " + str(self.depth) + ", Cost: " + str(self.cost)