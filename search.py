import game as g
import copy
import random
import queue


class StateNode:
    def __init__(self, game: g.Game8, parent, generator, depth, cost):
        self.game = game
        self.parent = parent
        self.generator = generator
        self.depth = depth
        self.cost = cost
        self.children = []

    def is_final_state(self):
        return self.game.check_win()

    # Generates a child node of the current state node based on an operation (in the case of the game movement in four possible directions)
    def generate_child(self, operator):
        child_game = copy.deepcopy(self.game)
        # If the move can't be done returns None
        if not child_game.move(operator):
            return None
        child = StateNode(child_game, self, operator, self.depth + 1, self.cost + 1)
        self.children.append(child)
        return child

    def generate_children(self):
        operators = [0, 1, 2, 3]
        random.shuffle(operators)
        for i in operators:
            child = self.generate_child(i)
        return self.children

    def toString(self):
        return "Generator: " + str(self.generator) + ", Depth: " + str(self.depth) + ", Cost: " + str(self.cost)


# Function for depth first search, returns the path (list of states) of the search
def depth_first_search(initial_state: StateNode):
    path_start = [initial_state]
    # Case where the initial state is the final state
    if initial_state.is_final_state():
        return path_start
    stack = initial_state.generate_children()
    next_state = stack.pop()
    while next_state:
        # Case where the final state is reached we end the loop
        if next_state.is_final_state():
            break
        # If the current state is the same as its grandparent, it skips to the next without generating its children
        if next_state.depth >= 2 and next_state.game == next_state.parent.parent.game:
            next_state = stack.pop()
            continue
        stack += next_state.generate_children()
        next_state = stack.pop()
    path_end = []
    while next_state.parent is not None:
        path_end = [next_state] + path_end
        next_state = next_state.parent
    path = path_start + path_end
    return path

# Function for breadth first search, returns the path list
def breadth_first_search(initial_state: StateNode):
    path_start = [initial_state]
    if initial_state.is_final_state():
        return path_start
    q = queue.Queue()
    initial_state.generate_children()
    for c in initial_state.children:
        q.put(c)
    next_state = q.get()
    while next_state:
        if next_state.is_final_state():
            break
        next_state.generate_children()
        for c in next_state.children:
            q.put(c)
        next_state = q.get()
    path_end = []
    while next_state.parent is not None:
        path_end = [next_state] + path_end
        next_state = next_state.parent
    path = path_start + path_end
    return path