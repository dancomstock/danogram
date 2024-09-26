class Game():

    _example_solution = [[1,1,0,1,1],
                       [1,1,0,1,1],
                       [0,0,1,0,0],
                       [0,0,1,0,0],
                       [1,1,1,1,1]]

    def __init__(self, solution):
        self.solution_rows = solution if solution else Game._example_solution
        self.input_rows = [[0 for box in rows] for rows in self.solution_rows]
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
        if counter:
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
        for row in puzzle_rows:
            if len(row) > max_length:
                max_length = len(row)

        for i, new_row in enumerate(new_rows):
            if len(new_row) < max_length:
                new_rows[i] = [' ' for x in range(max_length-1)] + new_row

        return new_rows

    def rows_to_columns(self, rows):
        return list(zip(*rows))

    def get_mark(self):
        try:
            mark_txt = input('input row,column\n')
            mark = mark_txt.split(',')
            y = int(mark[0])-1 if int(mark[0]) > 0 else None
            x = int(mark[1])-1 if int(mark[1]) > 0 else None
            self.input_rows[y][x] = 0 if self.input_rows[y][x] else 1
            self.input_columns = self.rows_to_columns(self.input_rows)
        except:
            pass
        return x, y

    def check_errors(self, line, solution_line):
        for i, box in enumerate(line):
            if line[i] and not solution_line[i]:
                return True
        return False
    
    def won(self):
        return self.input_rows == self.solution_rows

    def draw_board(self):
        RED = '\033[91m'
        END = '\033[0m'

        leftpad = '    '
        rowpadding = ' '.join([' ' for box in self.row_puzzle[0]])

        column_numbers = ''.join([
            f' {RED if self.check_errors(self.input_columns[i], self.solution_columns[i]) else ''}{i+1}{END} ' 
                for i, column in enumerate(self.columns_puzzle)])

        border_left = '_'.join(['_' for box in self.row_puzzle[0]])
        border_right = ''.join([f'___' for column in self.columns_puzzle])

        top_line = f'{leftpad}{rowpadding}{column_numbers}'
        print(top_line)

        top_border = f'{leftpad}{border_left}{border_right}'
        print(top_border)

        for j in range(len(self.columns_puzzle[0])):
            padding = ''.join(['  ' for x in self.row_puzzle[0]])
            puzzle = '  '.join([str(self.columns_puzzle[i][j]) for i in range(len(self.columns_puzzle))])
            column_hints = f'   |{padding}{puzzle}'
            print(column_hints)

        for i, row in enumerate(self.input_rows):
            row_number = i+1
            errors = RED if self.check_errors(row, self.solution_rows[i]) else ''
            puzzle = ' '.join(str(box) for box in self.row_puzzle[i])
            boxes = ''.join(['[O]' if box else '[ ]' for box in row])
            row_board = f'{errors}{row_number}{END}  |{puzzle}{boxes}'
            print(row_board)
