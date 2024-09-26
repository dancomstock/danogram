import app.game as game

game.draw_board()
while game.input_rows != game.solution_rows:
    x, y = game.get_mark()
    try:
        game.input_rows[y][x] = 0 if game.input_rows[y][x] else 1
    except:
        pass
    game.draw_board()
print('You Win!')