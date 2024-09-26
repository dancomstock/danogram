from app.game import Game

solution = [[1,0,1],
            [0,1,0],
            [1,0,1]]

game = Game(solution=solution)
game.draw_board()
while not game.won():
    x, y = game.get_mark()
    game.draw_board()
print('You Win!')