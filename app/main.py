from app.game import Game
import random
import os
from app.utils import load as load
from app.utils import save as save
from app.utils import load_progress as load_progress
from app.utils import save_progress as save_progress
import app.text as text

# solution = [[1,0,1],
#             [0,1,0],
#             [1,0,1]]

os.system('')

print(text.danogram)
selection = None
while True:
    try:
        selection = input('select an option:\n1. import puzzle\n2. load progress\n3. new random puzzle\n4. create puzzle\n5. exit\n')
        if selection == 'import' or selection == '1':
            save_txt = input('paste puzzle string\n')
            solution = load(save_txt)
            game = Game(solution=solution)
            game.play() if game else ''
        elif selection == 'load progress' or selection == '2':
            save_txt = input('paste save string\n')
            solution, progress = load_progress(save_txt)
            game = Game(solution=solution, progress=progress)
            game.play() if game else ''
        elif selection == 'random' or selection == '3':
            game = Game.new_random_game()
            game.play() if game else ''
        elif selection == 'create' or selection == '4':
            game = Game.new_blank_game()
            game.play() if game else ''
        elif selection == 'exit' or selection == '5':
            exit('game quit')

        else:
            print('invalid')
    except KeyboardInterrupt:
        exit('game quit')
    except Exception as e:
        print(f'Error: {e}')


# game = Game.new_random_game()
# game = Game(solution=solution)
game.play()