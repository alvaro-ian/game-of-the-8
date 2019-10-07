import game as g
import search as s

table1 = [[1, 3, 'b'], [4, 2, 8], [7, 5, 6]]
table2 = [[5, 'b', 2], [1, 4, 3], [7, 8, 6]]
table3 = [['b', 2, 3], [1, 5, 6], [4, 7, 8]]

#initial_state = s.StateNode(g.Game8(table1), None, None, 0, 0)
#initial_state = s.StateNode(g.Game8(table2), None, None, 0, 0)
initial_state = s.StateNode(g.Game8(table3), None, None, 0, 0)

#search = s.depth_first_search(initial_state)       # Not OK
#search = s.breadth_first_search(initial_state)     # OK
#search = s.greedy_search(initial_state)            # Not OK
search = s.a_star_search(initial_state)             # OK

for state in search:
    state.game.show_table()

print("Passos: " + str(search.__len__() - 1))