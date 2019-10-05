import game as g
import search as s

table2 = [[5, 'b', 2], [1, 4, 3], [7, 8, 6]]
table3 = [['b', 2, 3], [1, 5, 6], [4, 7, 8]]

#initial_state = s.StateNode(g.Game8(table2), None, None, 0, 0)
initial_state = s.StateNode(g.Game8(table3), None, None, 0, 0)

#search = s.depth_first_search(initial_state)
search = s.breadth_first_search(initial_state)

for state in search:
    state.game.show_table()

print(search.__len__())