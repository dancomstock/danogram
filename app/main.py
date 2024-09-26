from app.game import Game
import random

print(random.randint(3, 9))


# solution = [[1,0,1],
#             [0,1,0],
#             [1,0,1]]


game = Game.new_random_game()
# game = Game(solution=solution)
game.play()