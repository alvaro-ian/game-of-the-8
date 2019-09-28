import game as g
import search as s

table = [[1, 2, 3], [4, 5, 6], ['b', 8, 7]]

new_game = g.Game8(table)
'''
new_game.show_table()
while new_game.move(g.move_directions['UP']):
    new_game.show_table()
while new_game.move(g.move_directions['RIGHT']):
    new_game.show_table()
while new_game.move(g.move_directions['DOWN']):
    new_game.show_table()
while new_game.move(g.move_directions['LEFT']):
    new_game.show_table()

print(new_game.moves)'''

initial_state = s.StateNode(new_game, None, None, 0, 0)
print(initial_state.toString())

initial_state.game.show_table()

new_state = initial_state.generate_son(g.move_directions['DOWN'])

print(new_state)

new_state = initial_state.generate_son(g.move_directions['UP'])
new_state2 = initial_state.generate_son(g.move_directions['RIGHT'])

for i in range(len(initial_state.sons)):
    print(initial_state.sons[i].toString())
    initial_state.sons[i].game.show_table()

print(initial_state.sons)