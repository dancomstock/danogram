from app.utils import Color as color
from app.utils import load as load
from app.utils import save as save
from app.utils import load_progress as load_progress
from app.utils import save_progress as save_progress
import random

DEBUG = False

class Game:

    _example_solution = [[1,1,0,1,1],
                         [1,1,0,1,1],
                         [0,0,1,0,0],
                         [0,0,1,0,0],
                         [1,1,1,1,1]]
    
    @property
    def won(self):
        return self.input_rows == self.solution_rows
        
    def new_random_game(x=None,y=None):
        if not x or not y:
            try:
                size_text = input('input board x,y size\n')
                size = size_text.split(',')
                x = int(size[0])
                y = int(size[1])
            except:
                print('invalid input')
                return None
        solution = [[random.randint(0, 1) for i in range(x)] for i in range(y)]
        return Game(solution=solution)
    
    def new_blank_game(x=None,y=None):
        if not x or not y:
            try:
                size_text = input('input board x,y size\n')
                size = size_text.split(',')
                x = int(size[0])
                y = int(size[1])
            except:
                print('invalid input')
                return None
        solution = [[0 for i in range(x)] for i in range(y)]
        return Game(solution=solution, mode='edit')
    
    def load_edit_game(solution):
        return Game(solution=solution, mode='edit')
    
    def __init__(self, solution=None, progress=None, mode=None):
        self.mode = mode
        self.quit = False
        self.solution_rows = solution if solution else Game._example_solution
        self.input_rows = [[0 for box in rows] for rows in self.solution_rows] if not progress and solution else progress
        self.input_columns = self.rows_to_columns(self.input_rows)
        self.solution_columns = (self.rows_to_columns(self.solution_rows))
        self.columns_puzzle = self.generate_puzzle(self.solution_columns)
        self.columns_puzzle = self.add_spaces_to_puzzle(self.columns_puzzle)
        self.row_puzzle = self.generate_puzzle(self.solution_rows)
        self.row_puzzle = self.add_spaces_to_puzzle(self.row_puzzle)

    def check_line(self, line, solution_line):
        if line == solution_line:
            pass

    def generate_puzzle_line(self, line):
        counter = 0
        solution_line = []
        for box in line:
            if box == 1:
                counter += 1
            elif counter:
                solution_line.append(counter)
                counter = 0
        if counter or not solution_line:
            solution_line.append(counter)
        return solution_line

    def generate_puzzle(self, rows):
        row_solutions = []
        for row in rows:
            row_solutions.append(self.generate_puzzle_line(row))
        return row_solutions

    def add_spaces_to_puzzle(self, puzzle_rows):
        max_length = 0
        new_rows = puzzle_rows.copy()
        for i, row in enumerate(new_rows):
            for j, box in enumerate(row):
                if box >= 10:
                    new = str(box)
                    new_rows[i] = [*row[:j],'-',*new,'-',*row[j+1:]]
                
        for row in new_rows:
            if len(row) > max_length:
                max_length = len(row)

        for i, new_row in enumerate(new_rows):
            if len(new_row) < max_length:
                new_rows[i] = [' ' for x in range(max_length-len(new_row))] + new_row

        return new_rows

    def rows_to_columns(self, rows):
        return list(zip(*rows))

    def get_mark(self):
        try:
            mark_txt = input('input row,column to mark or unmark\ninput save to save progress\n')
            if mark_txt == 'save':
                print('save below text:\n')
                if self.mode == 'edit':
                    print(save(self.input_rows))
                else:
                    print(save_progress(self.solution_rows, self.input_rows))
                print('\nsave above text\n')
                self.quit = True
                return None, None
            elif mark_txt == 'quit':
                print('\nquit to menu\n')
                self.quit = True
                return None, None
            else:
                mark = mark_txt.split(',')
                y = int(mark[0])-1 if int(mark[0]) > 0 else None
                x = int(mark[1])-1 if int(mark[1]) > 0 else None
                self.input_rows[y][x] = 0 if self.input_rows[y][x] else 1
                self.input_columns = self.rows_to_columns(self.input_rows)
        except KeyboardInterrupt:
            exit('game quit')
        except Exception as e:
            print(f'{color.red}invalid input{color.end} {e if DEBUG else ''}')
            return None, None
        return x, y

    def check_errors(self, line, solution_line):
        for i, box in enumerate(line):
            if line[i] and not solution_line[i]:
                return True
        return False

    def _get_digit(self, number, digit):
        try:
            return str(number)[-digit]
        except:
            return ' '
        
    def _edit_mode_update(self):
        self.solution_rows = self.input_rows
        self.input_columns = self.rows_to_columns(self.input_rows)
        self.solution_columns = (self.rows_to_columns(self.solution_rows))
        self.columns_puzzle = self.generate_puzzle(self.solution_columns)
        self.columns_puzzle = self.add_spaces_to_puzzle(self.columns_puzzle)
        self.row_puzzle = self.generate_puzzle(self.solution_rows)
        self.row_puzzle = self.add_spaces_to_puzzle(self.row_puzzle)

    def draw_board(self):
        row_number_max_digits = len(str(len(self.input_rows)))
        col_number_max_digits = len(str(len(self.input_rows)))
        leftpad = '   ' + ''.join([' ' for n in range(row_number_max_digits)])
        rowpadding = ' '.join([' ' for box in self.row_puzzle[0]])
        border_left = '_'.join(['_' for box in self.row_puzzle[0]])
        border_right = ''.join([f'___' for column in self.columns_puzzle])

        
        for n in range(col_number_max_digits-1,-1,-1):
            column_numbers = ''.join([
                f' {color.red if self.check_errors(self.input_columns[i], self.solution_columns[i]) else ''}{self._get_digit(i+1,n+1)}{color.end} ' 
                    for i, column in enumerate(self.columns_puzzle)])
            top_line = f'{leftpad}{rowpadding}{column_numbers}'
            print(top_line)

        top_border = f'{leftpad}{border_left}{border_right}'
        print(top_border)

        for j in range(len(self.columns_puzzle[0])):
            leftpad = '  ' + ''.join([' ' for n in range(row_number_max_digits)])
            padding = ''.join(['  ' for x in self.row_puzzle[0]])
            puzzle = '  '.join([str(self.columns_puzzle[i][j]) for i in range(len(self.columns_puzzle))])
            column_hints = f'{leftpad}|{padding}{puzzle}'
            print(f'{column_hints}')

        for i, row in enumerate(self.input_rows):
            row_number = i+1
            row_number_digits = len(str(row_number))
            row_number_range = range(row_number_max_digits-row_number_digits)
            row_number_padded =  ''.join([' ' for n in row_number_range]) + str(row_number)
            errors = color.red if self.check_errors(row, self.solution_rows[i]) else ''
            puzzle = ' '.join(str(box) for box in self.row_puzzle[i])
            boxes = ''.join(['[O]' if box else '[ ]' for box in row])
            row_board = f'{errors}{row_number_padded}{color.end}  |{puzzle}{boxes}'
            print(row_board)

    def play(self):
        if DEBUG:
            print(f'mode={self.mode}')
        if self.mode == 'edit':
            while not self.quit:
                self.draw_board()
                x, y = self.get_mark()
                self._edit_mode_update()
                
        else:
            while not self.won and not self.quit:
                self.draw_board()
                x, y = self.get_mark()
            if not self.quit:
                self.draw_board()
                print('You Win!')