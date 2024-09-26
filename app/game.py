

def check_line(line, solution_line):
    if line == solution_line:
        pass

def generate_puzzle_line(line):
    # print(f'line:{line}')
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

def generate_puzzle(rows):
    row_solutions = []
    for row in rows:
        row_solutions.append(generate_puzzle_line(row))
    return row_solutions

def add_spaces_to_puzzle(puzzle_rows):
    max_length = 0
    new_rows = puzzle_rows.copy()
    for row in puzzle_rows:
        if len(row) > max_length:
            max_length = len(row)

    for i, new_row in enumerate(new_rows):
        if len(new_row) < max_length:
            new_rows[i] = [' ' for x in range(max_length-1)] + new_row

    return new_rows


def rows_to_columns(rows):
    # columns = [['x' for row in rows] for row in rows]
    # print(columns)
    # for i in range(len(rows)):
    #     print(f'i:{i}--------------------------------')
    #     for j in range(len(rows[i])):
    #         print(f'j:{j}')
    #         # print(f'row:{rows[i]}')
    #         print(f'select:{rows[i][j]}')
    #         columns[j][i] = rows[i][j]
    #         # print(f'column:{columns[j]}')

    # return columns
    return list(zip(*rows))







solution_rows = [[1,1,0,1,1],
                 [1,1,0,1,1],
                 [0,0,1,0,0],
                 [0,0,1,0,0],
                 [1,1,1,1,1]]

# solution_rows = [[1,1,0,1,1],
#                  [1,1,0,1,1],
#                  [0,0,1,0,0],
#                  [0,0,1,0,0],
#                  [1,1,1,1,1],
#                  [1,1,1,1,0]]

# solution_rows = [[1,1,0],
#                  [1,1,0],
#                  [0,0,1]]


input_rows = [[0 for box in rows] for rows in solution_rows]
# print(f'input row:{input_rows}')

expected_columns = [[1,1,0,0,1],
                    [1,1,0,0,1],
                    [0,0,1,1,1],
                    [1,1,0,0,1],
                    [1,1,0,0,1]]

rows2 = ['2-2',
         '2-2',
         '1',
         '1',
         '5']

rows3 = [[2,2],[2,2],[1],[1],[5]]


# columns = rows_to_columns(rows)
solution_columns = (rows_to_columns(solution_rows))
columns_puzzle = generate_puzzle(solution_columns)
columns_puzzle = add_spaces_to_puzzle(columns_puzzle)
row_puzzle = generate_puzzle(solution_rows)
row_puzzle = add_spaces_to_puzzle(row_puzzle)
# print(columns)
# for i in range(len(columns)):

# for j in range(len(columns[0])):
#     print(''.join(['  ' for x in row_puzzle[0]]) + '  '.join([str(columns[i][j]) for i in range(len(columns))]))
# # print(' ' + '  '.join([str(columns[i][1]) for i in range(len(columns))]))6,

# for column in columns:
#     pass



# for i, row in enumerate(solution_rows):
#     print(f'{' '.join(str(box) for box in row_puzzle[i]) + ''.join(['[O]' if box else '[ ]' for box in row])}')


def get_mark():
    mark_txt = input('input row,column\n')
    mark = mark_txt.split(',')
    y = int(mark[0])-1 if int(mark[0]) > 0 else None
    x = int(mark[1])-1 if int(mark[1]) > 0 else None
    print(f'x:{mark[1]} y:{mark[0]}')
    return x, y

def check_errors(line, solution_line):
    for i, box in enumerate(line):
        if line[i] and not solution_line[i]:
            return True
    return False

def draw_board():
    RED = '\033[91m'
    END = '\033[0m'

    input_columns = rows_to_columns(input_rows)
    leftpad = '    '
    rowpadding = ' '.join([' ' for box in row_puzzle[0]])

    # er = RED if check_errors(input_columns[i], solution_columns[i]) else None

    column_numbers = ''.join([
        f' {RED if check_errors(input_columns[i], solution_columns[i]) else ''}{i+1}{END} ' 
            for i, column in enumerate(columns_puzzle)])

    line = '_'.join(['_' for box in row_puzzle[0]])
    # line2 = ''.join([f'_{'X' if check_errors(input_columns[i], solution_columns[i]) else '_'}_' for i, column in enumerate(columns)])
    line2 = ''.join([f'___' for column in columns_puzzle])
    


    print(f'{leftpad}{rowpadding}{column_numbers}')
    # print(f'    {' '.join([' ' for box in row_puzzle[0]])}{''.join([f'   ' for i, column in enumerate(columns)])}')

    print(f'{leftpad}{line}{line2}')
    for j in range(len(columns_puzzle[0])):
        print(f'   |{''.join(['  ' for x in row_puzzle[0]]) + '  '.join([str(columns_puzzle[i][j]) for i in range(len(columns_puzzle))])}')

    for i, row in enumerate(input_rows):
        row_number = i+1
        # errors = 'X' if check_errors(row, solution_rows[i]) else ' '
        errors = RED if check_errors(row, solution_rows[i]) else ''
        puzzle = ' '.join(str(box) for box in row_puzzle[i])
        boxes = ''.join(['[O]' if box else '[ ]' for box in row])
        # print(f'{row_number} {errors}|{puzzle}{boxes}')
        print(f'{errors}{row_number}{END}  |{puzzle}{boxes}')
        # print(f'{i+1} {'X' if check_errors(row, solution_rows[i]) else ' '}|{' '.join(str(box) for box in row_puzzle[i]) + ''.join(['[O]' if box else '[ ]' for box in row])}')


draw_board()
while input_rows != solution_rows:
    x, y = get_mark()
    try:
        input_rows[y][x] = 0 if input_rows[y][x] else 1
    except:
        pass
    draw_board()
print('You Win!')