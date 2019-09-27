import game as g

table = [[1, 2, 3], [4, 5, 6], ['b', 8, 7]]

new_game = g.Game8(table)

new_game.show_table()
while new_game.move(g.move_directions['UP']):
    new_game.show_table()
while new_game.move(g.move_directions['RIGHT']):
    new_game.show_table()
while new_game.move(g.move_directions['DOWN']):
    new_game.show_table()
while new_game.move(g.move_directions['LEFT']):
    new_game.show_table()

print(new_game.moves)