# Create the pieces

list_of_pieces = [
     [[0], [0, 0, 0, 0]],
     [[0, 0]],
     [[0, 0, 1], [1, 0]],
     [[1, 0, 0], [0, 1]],
     [[0, 0, 0], [1, 0], [1, 0, 1], [0, 1]],
     [[0, 0, 0], [2, 0], [0, 1, 1], [0, 0]],
     [[0, 0, 0], [0, 0], [1, 1, 0], [0, 2]]]

number_of_columns = 7
board = [0, 0, 0, 0, 0, 0, 0]

selected_piece = int(input()) - 1

column = 0
while column < number_of_columns:
    rotation = 0
    while rotation < len(list_of_pieces[selected_piece]):
        # Find the base
        base = list_of_pieces[selected_piece][rotation].index(0)
        if column < base:
            # The piece will not fit with the base in this position
            break
        current_column_height = board[column]
        evaluated_column = 0
        while evaluated_column < len(list_of_pieces[selected_piece][rotation])
            
            
            
        rotation += 1
    column += 1