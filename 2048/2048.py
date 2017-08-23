# Reading the input lines
board = list(map(lambda str_to_int: list(map(int, str_to_int)),
    [input().split(), input().split(), input().split(), input().split()]))

direction = input()

if direction == '0': #left move
    for row in board:
        columnbase = 0
        while columnbase < 4:
            columneval = columnbase + 1
            while columneval < 4:
                if row[columnbase] == 0: # tile is empty
                    if row[columneval] != 0:
                        row[columnbase] = row[columneval]
                        row[columneval] = 0
                elif row[columnbase] == row[columneval]:
                    row[columnbase] += row[columnbase]
                    row[columneval] = 0
                    break
                elif row[columneval] != 0:
                    break
                columneval += 1
            columnbase += 1
elif direction == '1': # up move
    for column in range(4): # We're iterating the columns one by one.
        rowbase = 0
        while rowbase < 4:
            roweval = rowbase + 1
            while roweval < 4:
                if board[rowbase][column] == 0: #Empty tile
                    if board[roweval][column] != 0:
                        board[rowbase][column] = board[roweval][column]
                        board[roweval][column] = 0
                elif board[rowbase][column] == board[roweval][column]:
                    board[rowbase][column] += board[rowbase][column]
                    board[roweval][column] = 0
                    break
                elif board[roweval][column] != 0:
                    break
                roweval += 1
            rowbase += 1
elif direction == '2': # right move
    for row in board:
        columnbase = 3
        while columnbase >= 0:
            columneval = columnbase - 1
            while columneval >= 0:
                if row[columnbase] == 0: # tile is empty
                    if row[columneval] != 0:
                        row[columnbase] = row[columneval]
                        row[columneval] = 0
                elif row[columnbase] == row[columneval]:
                    row[columnbase] += row[columnbase]
                    row[columneval] = 0
                    break
                elif row[columneval] != 0:
                    break
                columneval -= 1
            columnbase -= 1
elif direction == '3': # down move
    for column in range(4): # We're iterating the columns one by one.
        rowbase = 3
        while rowbase >= 0:
            roweval = rowbase - 1
            while roweval >= 0:
                if board[rowbase][column] == 0: #Empty tile
                    if board[roweval][column] != 0:
                        board[rowbase][column] = board[roweval][column]
                        board[roweval][column] = 0
                elif board[rowbase][column] == board[roweval][column]:
                    board[rowbase][column] += board[rowbase][column]
                    board[roweval][column] = 0
                    break
                elif board[roweval][column] != 0:
                    break
                roweval -= 1
            rowbase -= 1

for row in board:
    for number in row:
        print(number, end = " ")
    print()