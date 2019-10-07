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


generated_nodes = 0
state_border = 0
max_depth = 0

def start_test_variables():
    global generated_nodes, state_border, max_depth
    generated_nodes = 0
    state_border = 0
    max_depth = 0

# Function for depth first search, returns the path (list of states) of the search
def depth_first_search(initial_state: StateNode):
    global generated_nodes, state_border, max_depth
    start_test_variables()
    path_start = [initial_state]
    # Case where the initial state is the final state
    if initial_state.is_final_state():
        return path_start
    stack = initial_state.generate_children()
    generated_nodes += len(initial_state.children)
    next_state = stack.pop()
    while next_state:
        if next_state.depth > max_depth:
            max_depth = next_state.depth
        # Case where the final state is reached we end the loop
        if next_state.is_final_state():
            break
        # If the current state is the same as its grandparent, it skips to the next without generating its children
        if next_state.depth >= 2 and next_state.game == next_state.parent.parent.game:
            next_state = stack.pop()
            continue
        stack += next_state.generate_children()
        generated_nodes += len(next_state.children)
        next_state = stack.pop()
    state_border = len(stack)
    path_end = []
    while next_state.parent is not None:
        path_end = [next_state] + path_end
        next_state = next_state.parent
    path = path_start + path_end
    return path

# Function for breadth first search, returns the path list
def breadth_first_search(initial_state: StateNode):
    global generated_nodes, state_border, max_depth
    start_test_variables()
    path_start = [initial_state]
    if initial_state.is_final_state():
        return path_start
    q = queue.Queue()
    initial_state.generate_children()
    generated_nodes += len(initial_state.children)
    for c in initial_state.children:
        q.put(c)
    next_state = q.get()
    while next_state:
        if next_state.depth > max_depth:
            max_depth = next_state.depth
        if next_state.is_final_state():
            break
        next_state.generate_children()
        generated_nodes += len(next_state.children)
        for c in next_state.children:
            q.put(c)
        next_state = q.get()
    state_border = q.qsize()
    path_end = []
    while next_state.parent is not None:
        path_end = [next_state] + path_end
        next_state = next_state.parent
    path = path_start + path_end
    return path

# Heuristic function for the heuristic searches, the method used was the sum of the distance of the numbers
# from their end location on the table
def heuristic_function(state: StateNode):
    end_game = g.Game8(g.end_table)
    h = 0
    for i in range(len(state.game.table)):
        for j in range(len(state.game.table[i])):
            pos = end_game.get_position(state.game.table[i][j])
            h += abs(i - pos[g.line]) + abs(j - pos[g.column])
    state.cost += h
    return state.cost

# Function for greedy search based on the above heuristic function
def greedy_search(initial_state: StateNode):
    global generated_nodes, state_border, max_depth
    start_test_variables()
    path_start = [initial_state]
    if initial_state.is_final_state():
        return path_start
    stack = initial_state.generate_children()
    generated_nodes += len(initial_state.children)
    less_cost = 1000
    next_state = None
    step_state = None
    for state in stack:
        heuristic_function(state)
        if state.cost < less_cost:
            less_cost = state.cost
            step_state = next_state
            next_state = state
    stack.clear()
    while next_state:
        if next_state.depth > max_depth:
            max_depth = next_state.depth
        if next_state.is_final_state():
            break
        if next_state.depth >= 2 and next_state.game.table == next_state.parent.parent.game.table:
            next_state = step_state
            continue
        stack = next_state.generate_children()
        generated_nodes += len(next_state.children)
        less_cost = 1000
        for state in stack:
            heuristic_function(state)
            if state.cost < less_cost:
                less_cost = state.cost
                next_state = state
        stack.clear()
    state_border = len(stack)
    path_end = []
    while next_state.parent is not None:
        path_end = [next_state] + path_end
        next_state = next_state.parent
    path = path_start + path_end
    return path

# Function for A* search based on the heuristic function above
def a_star_search(initial_state: StateNode):
    global generated_nodes, state_border, max_depth
    start_test_variables()
    path_start = [initial_state]
    if initial_state.is_final_state():
        return path_start
    q = initial_state.generate_children()
    generated_nodes += len(initial_state.children)
    less_cost = 1000
    next_state = None
    for state in q:
        heuristic_function(state)
        if state.cost < less_cost:
            less_cost = state.cost
            next_state = state
    q.remove(next_state)
    while next_state:
        if next_state.depth > max_depth:
            max_depth = next_state.depth
        if next_state.is_final_state():
            break
        aux = next_state.generate_children()
        generated_nodes += len(next_state.children)
        for state in aux:
            heuristic_function(state)
        q += aux
        less_cost = 1000
        for state in q:
            if state.cost < less_cost:
                less_cost = state.cost
                next_state = state
        q.remove(next_state)
    state_border = len(q)
    path_end = []
    while next_state.parent is not None:
        path_end = [next_state] + path_end
        next_state = next_state.parent
    path = path_start + path_end
    return path